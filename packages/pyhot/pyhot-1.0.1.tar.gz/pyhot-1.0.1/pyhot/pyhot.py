import importlib
import sys
import inspect
import copy
import os

can_copy_type = [type(1),type(""),type([]),type({})]


# 热更对象
class HotObj():
    def __init__(self):
        # 添加到热更管理器
        if hot_mgr.need_add:
            hot_mgr.add_obj(self)
            
# 文件对象
class FileObj():
    path = ""
    time = 0
    mod = ""
    def __init__(self, file_path, mod_name):
        self.path = file_path
        self.mod = mod_name
        self.time = os.stat(file_path).st_mtime

# 热更管理器
class HotMgr():
    obj_map = {}            # 对象map
    need_add = True         # 是否需要加到管理
    
    file_map = {}           # 文件map
    def __init__(self):
        self.obj_map = {}
        
    # 添加新对象
    def add_obj(self, obj):
        # 添加到对应列表中
        class_name = str(obj.__class__)
        if class_name not in self.obj_map:
            self.obj_map[class_name] = []
        self.obj_map[class_name].append(obj)
    
    # 获取模块文件对象
    def get_file_obj(self, mod_name):
        if mod_name in self.file_map:
            return self.file_map[mod_name]
        else:
            importlib.import_module(mod_name)
            mod = sys.modules[mod_name]
            file_obj = FileObj(mod.__file__, mod_name)
            file_obj.time = 0
            self.file_map[mod_name] = file_obj
            return file_obj
    
    # 地址转模块名格式
    def path_to_mod_name(self, path:str):
        # 去掉前面的 ./
        if path.find("./") == 0:
            path = path[2:]
        path = path.replace("\\", ".")
        path = path.replace("/", ".")
        end_idx = path.rfind(".")
        path = path[:end_idx]
        return path
    
    # 初始化文件变化记录
    def init_file_record(self):
        for root, dirs, files in os.walk("./", topdown=False):
            for name in files:
                # 跳过文件 没有后缀、不是py文件、.开头、_开头
                end_idx = name.rfind(".")
                if end_idx < 0 or name[end_idx:] != ".py" or name[0] == "." or name[0] == "_":
                    continue
                file_path = os.path.join(root, name)
                mod_name = self.path_to_mod_name(file_path)
                file_obj = FileObj(file_path, mod_name)
                self.file_map[mod_name] = file_obj
    
    # 热更目录下文件
    def hot_all(self):
        for root, dirs, files in os.walk("./", topdown=False):
            for name in files:
                # 跳过文件 没有后缀、不是py文件、.开头、_开头
                end_idx = name.rfind(".")
                if end_idx < 0 or name[end_idx:] != ".py" or name[0] == "." or name[0] == "_":
                    continue
                file_path = os.path.join(root, name)
                mod_name = self.path_to_mod_name(file_path)
                # 不在map不需要热更， 修改时间一致不需要热更
                if mod_name not in self.file_map or self.file_map[mod_name].time == os.stat(file_path).st_mtime:
                    # 更新file_obj
                    file_obj = FileObj(file_path, mod_name)
                    self.file_map[mod_name] = file_obj
                    continue
                else:
                    self.hot(mod_name)
    
    # 热更模块
    def hot(self, mod_name):
        file_obj = self.get_file_obj(mod_name)
        # 是否有变化
        now_time = os.stat(file_obj.path).st_mtime
        if file_obj.time == now_time:
            return
        file_obj.time = now_time
        
        # 重载模块
        mod = sys.modules[mod_name]
        importlib.reload(mod)
        # 热更类对象
        self.need_add = False
        class_list = inspect.getmembers(mod, inspect.isclass)
        for class_item in class_list:
            class_obj = class_item[1]
            class_name = str(class_item[1])
            if class_name not in self.obj_map:
                continue
            else:
                new_class_obj = class_obj()
                fun_list = inspect.getmembers(class_obj, inspect.isfunction)
                fun_name_list = []
                for tmp_fun in fun_list:
                    fun_name_list.append(tmp_fun[0])
                
                # 遍历类属性
                for class_attr_k in class_obj.__dict__:
                    # 跳过内部属性
                    if class_attr_k.startswith('__'):
                        continue
                    
                    new_class_obj_attr = getattr(new_class_obj, class_attr_k)
                    new_class_obj_attr_type = type(new_class_obj_attr)
                    # 如果是函数
                    if class_attr_k in fun_name_list:
                        for tmp_obj in self.obj_map[class_name]:
                            # 这步是重点，对__class__操作
                            setattr(tmp_obj.__class__, class_attr_k, getattr(class_obj, class_attr_k))
                    # 是否是可以更新的类型
                    elif new_class_obj_attr_type in can_copy_type:
                        # 如果不在旧对象中，或类型不对
                        for tmp_obj in self.obj_map[class_name]:
                            if class_attr_k not in tmp_obj.__dict__ or type(new_class_obj_attr) != type(getattr(tmp_obj, class_attr_k)):
                                new_attr = copy.deepcopy(new_class_obj_attr)
                                setattr(tmp_obj, class_attr_k, new_attr)
                # print("hot class:%s, num:%s"%(class_name, len(self.obj_map[class_name])))
        self.need_add = True
hot_mgr = HotMgr()
