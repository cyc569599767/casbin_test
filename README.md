## casbin支持的 models



1. ACL (Access Control List, 访问控制列表
2. **具有 超级用户 的 ACL**
3. **没有用户的 ACL**: 对于没有身份验证或用户登录的系统尤其有用。
4. **没有资源的 ACL**: 某些场景可能只针对资源的类型, 而不是单个资源, 诸如 `write-article`, `read-log`等权限。 它不控制对特定文章或日志的访问。
5. **RBAC (基于角色的访问控制)**
6. **支持资源角色的RBAC**: 用户和资源可以同时具有角色 (或组)。
7. **支持域/租户的RBAC**: 用户可以为不同的域/租户设置不同的角色集。
8. **ABAC (基于属性的访问控制)**: 支持利用`resource.Owner`这种语法糖获取元素的属性。
9. **RESTful**: 支持路径, 如 `/res/*`, `/res/: id` 和 HTTP 方法, 如 `GET`, `POST`, `PUT`, `DELETE`。
10. **拒绝优先**: 支持允许和拒绝授权, 拒绝优先于允许。
11. **优先级**: 策略规则按照先后次序确定优先级，类似于防火墙规则。



## models 访问控制模型文件

- Model CONF 至少应包含四个部分: `[request_definition], [policy_definition], [policy_effect], [matchers]`。
- 如果 model 使用 RBAC, 还需要添加`[role_definition]`部分。
- Model CONF 文件可以包含注释。注释以 `#` 开头， `#` 会注释该行剩余部分

```ini
[request_definition]
# request 定义
# sub, obj, act 表示经典三元组: 访问实体 (Subject)，访问资源 (Object) 和访问方法 (Action)。 但是, 你可以自定义你自己的请求表单, 如果不需要指定特定资源，则可以这样定义 sub、act ，或者如果有两个访问实体, 则为 sub、sub2、obj、act。
# 明确了 e.enforce(...) 函数中参数的含义
r = sub, obj, act

[policy_definition]
# policy 策略
# 定义访问策略的模型。其实就是定义Policy规则文档中各字段的名称和顺序。
# 如果不定义 eft(策略结果)，那么将不会去读策略文件中的结果字段，并将匹配的策略结果都默认为allow。
p = sub, obj, act, eft

[role_definition]
# 角色定义
g = _, _, _
g2 = _, _
# 上述角色定义表明, g 是一个 RBAC系统, g2 是另一个 RBAC 系统。
# _, _表示角色继承关系的前项和后项，即前项继承后项角色的权限, 前项是后项的一个成员.
# 第三个 _ 表示域/租户的名称, 此部分不应更改.表示 前项在域内具有后项角色.

[matchers]
# Matchers 匹配规则
# 定义了策略匹配者。匹配者是一组表达式。它定义了如何根据请求来匹配策略规则.
# Request和Policy的匹配规则。
m = g(r.sub, p.sub) && r.obj == p.obj && r.act == p.act
# 上述定义表明,请求中的 sub 必须有 policy 中的 sub 角色
```

## 角色层次

Casbin 的 RBAC 支持 RBAC1 的角色层次结构功能，如果 `alice`具有`role1`, `role1`具有`role2`，则 `alice` 也将拥有 `role2` 并继承其权限。

## 如何区分用户和角色？

在RBAC中，Casbin不对用户和角色进行区分。 它们都被视为字符串。 如果你只使用单层的RBAC模型（角色不会成为另一个角色的成员）。 可以使用 `e.GetAllSubjects()` 获取所有用户，`e.GetAllRoles()` 获取所有角色。 它们会为规则 `g, u, r` 分别列出所有的 `u` 和 `r`。



# 总结:
当前 pycasbin 版本为 0.10.0  不支持 ABAC 模式的 eval 函数,无法解析 policy 策略.咱不能使用