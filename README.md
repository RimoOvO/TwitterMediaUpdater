# TwitterMediaUpdater
基于Chrome插件（[Twitter Media Downloader](https://chrome.google.com/webstore/detail/twitter-media-downloader/cblpjenafgeohmnjknfhpdbdljfkndig)）的媒体下载和自动增量更新自动化脚本

# 准备工作
1. Chrome浏览器，并安装对应版本的[Chromedriver](https://registry.npmmirror.com/binary.html?path=chromedriver/)
2. 一个Twitter账号
3. Python 3.9
4. 需要自行安装的python组件：selenium、retrying

# 使用方法

1. 将本项目所有文件单独存放在一个文件夹中，并将这个文件夹再放进另一个文件夹中。因为下载的媒体保存位置在项目文件夹的上一层。
2. 进入项目文件夹，在命令行中运行`uid.py`,在其中输入要下载的用户的id，不需要加@符号，它会自己检查是否已经添加过，并以文本文件的形式保存到`uid.txt`中，以逗号分隔。
3. 打开`update.py`文件，并修改文件开头用注释标注范围内的信息。`service_path`后面的路径为你安装的`chromedriver.exe`的可执行文件路径。`email`、`username`、`password`、`phone_number`都为你的Twitter账号信息，精力有限暂都以明文储存，请注意信息安全。`download_path`为你的Chrome浏览器的下载路径文件夹，**以斜杠/结尾**。
4. 进入项目文件夹，在命令行中运行`update.py`,他将会自动登录并进入到用户主页，使用插件`Twitter Media Downloader`进行下载，媒体将会保存到项目的上一级文件夹中，以用户名命名。
5. 如果要进行增量更新，再运行一次`update.py`即可，他会自动读取上一次保存的最后一个时间戳，填入插件的时间戳范围内，以下载更新的新的媒体内容

# 致谢
本项目使用了Chrome插件[Twitter Media Downloader](https://chrome.google.com/webstore/detail/twitter-media-downloader/cblpjenafgeohmnjknfhpdbdljfkndig)作为下载核心组件
