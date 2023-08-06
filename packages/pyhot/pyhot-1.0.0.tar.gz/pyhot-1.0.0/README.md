# hotpy
热更python的class对象
已经存在的也会更新已有的属性和函数，没有则会添加新的class的属性和函数

已提供pip安装 项目中引用即可  
`pip install hotpy`

# 使用方法
在需要热更的类中继承hotpy.HotObj
调用hotpy.hot_mgr.hot(mod_name)
会热更mod和它里面的类对象
