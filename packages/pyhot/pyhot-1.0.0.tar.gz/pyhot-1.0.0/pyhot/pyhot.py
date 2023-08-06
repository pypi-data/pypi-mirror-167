import importlib
import sys
import inspect
import copy

can_copy_type = [type(1),type(""),type([]),type({})]


# 热更对象
class HotObj():
    def __init__(self):
        # 添加到热更管理器
        if hot_mgr.need_add:
            hot_mgr.add_obj(self)

# 热更管理器
class HotMgr():
    obj_map = {}            # 对象map
    need_add = True         # 是否需要加到管理
    def __init__(self):
        self.obj_map = {}
        
    # 添加新对象
    def add_obj(self, obj):
        # 添加到对应列表中
        class_name = str(obj.__class__)
        if class_name not in self.obj_map:
            self.obj_map[class_name] = []
        self.obj_map[class_name].append(obj)

    # 开始热更
    def hot(self, file_name):
        if file_name not in sys.modules:
            importlib.import_module(file_name)
        # 重载模块
        mod = sys.modules[file_name]
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
