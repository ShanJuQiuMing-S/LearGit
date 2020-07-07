'''
今天下载了一个git，安装之后发现找不到app。然后在简书上找到一位博主的文章，顺利解决应用问题。虽然比较简单，还是很开心。以后要开启在git学习之旅，上向大佬们学习啦！简书博主链接https://www.jianshu.com/p/7edb6b838a2e。希望能帮助到各位小伙伴们。嘻嘻

'''
## 1.git安装之后，在终端设置name、email、ssh_key
git config --global user.name "name"            # 设置用户名
git config --global user.email "email@xx.com"   # 设置邮箱
ssh-keygen -t rsa -C "email@xx.com"             # 创建ssh_key
open .ssh/id_rsa.pub           # 查看ssh_key
ssh -T git@github.com          # 验证链接是否成功
# 创建项目，克隆SSH后，开始上传已有的文件
cd /Users/XXXXXXX/Desktop/     # 切换到桌面
git clone git@github.com:ShanJuQiuMing-S/LearGit.git  # 克隆SSH，让通知git上传项目地址，SSH：git@github.com:ShanJuQiuMing-S/LearGit.git
# 在桌面创建上传文件，初始设置的是.py,准备好上传的文件后可以进行以下操作。
cd /Users/XXXXXXX/Desktop/目标文件夹 
git add .                      # '.'代表所有文件，这行代码的意思是把所有的文件添加到仓库
git commit -m 'first commit'   # 文件提交到仓库，其中‘ -m ’代表注释，引号里面是主食内容
git push                       # 上传到github



## 2.怎样和同事协作项目操作
## 在终端切换到当前目录的指定文件夹
cd ~                            # ‘～’ 指定路径
git config --global user.name 'name'
git config --global user.email 'xx@jjjj.com'
git config -l                   # 查看设置
git init                        # 项目初始化
git remote add origin + ‘SSH’   # git与github连接
git status                      # 查看git下的文件
git add *                       # 文件添加仓库
git commit -m ''                # 让文件在本地生效
git push -u origin master       # 文件上传到远端
## 同事z是怎样对组长的项目加工上传？
# 在github上搜索项目---〉把组长的项目copy到本地：fork---〉找到文件--—〉 点击文件后面的图标j修改---〉commit ---〉点击pull request ---〉new pull request---〉 creat pull request ---〉 creat pull request ---〉等待组长审核
# 组长操作
# 刷新 ---〉 pull request---〉点开查看 ---〉merge pull request---〉 merge ---〉 commit



