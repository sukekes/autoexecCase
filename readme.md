# UI 自动化测试PageObject 实例

## 自动执行测试业务系统用例脚本
登录系统进入进入我的任务--用例执行页面，执行测试用例。先查找失败的用例执行，再查找阻塞的用例执行，最后执行通过的用例。

## 运行脚本步骤
### 1、打开pages/basepage.py ，修改base_url
~~~
self.base_url = "测试业务系统URL"
~~~
### 2、打开testdate/loginpage/login_by_manager.yml文件
在input_params下输入用户名、密码
~~~
input_params:
  username: "用户名"
  password: "密码"
~~~
### 3、打开testdata/personalwork/personal_work.yml文件
在input_params下输入项目名称
~~~
input_params:
  "sendkeys": "项目名称"
~~~
### 4、打开testdata/execc/execc.yml文件
在input_params下分别输入执行失败、阻塞、通过的用例编号。其中失败、阻塞的用例编号需要全部列出，通过的用例只需要列出用例编号最大值即可。
例如共计150条用例，从第141条用例开始是测试通过的，则通过用例只需要列出C141即可。
~~~
input_params:
  fault:
    - C1
    - C3
  block:
    - C11
    - C12
  sucess:
    - C116
~~~
### 5、执行run_test/run.py脚本
~~~
if __name__ == "__main__":
    pytest.main(["-m", "tasks"])
~~~

## 难点以及遇到的问题
### 1、用例执行标签无法直接定位
通过xpath进行定位，先定位用例编号，在定位用例编号的兄弟节点操作列，再定位操作列的子节点"执行”
~~~
//td[@title='C1']/following::td[@title='查看执行']/child::a[text()='执行']
~~~
### 2、页面内容变化后无法定位
~~~
org.openqa.selenium.StaleElementReferenceException: stale element reference: element is not attached to the page document
~~~
以上报错信息通过刷新页面解决
~~~
driver.refresh()
~~~
### 3、用例执行页面，内容无法加载出来，无法正常跳转
增加等待时间
~~~
sleep(2)
~~~

## 已知问题和注意事项
1、需要查询的用例（即execc.yml中填写的用例）均需要保证为待提交状态，否则会因为定位不到元素执行失败

2、当前未提供选择版本功能，默认执行最新版本的用例

3、执行execute_script返回None，暂未解决
~~~
code_value = execc.execute_script("return document.getElementById('code').value")
~~~

## 框架代码结构、依赖环境
相关内容参见：[PageObject实例](https://github.com/sukekes/autotestUI)
