# 通信加密服务站

#### 介绍
利用flask和pycryptodome来加密通信的内容,加密后服务器不会留下记录,同时https可以保护表单不受到监听,从而实现两个人通信内容加密的作用,实际用途不大，但是如果你想搞事情额.......可以考虑使用....

#### 软件架构
使用python3和pycryptodome、flask库,同时使用OpenSSL生成的证书。


#### 安装教程

1.  下载python3并安装,3.6版本以上
2.  pip  install pycryptodome
3.   pip install flask
本程序的证书来自OpenSSL生成的,你可以更换自己的证书。
QQ等通信方式并非端到端加密,你可以在任何不安全的平台上面,使用加密算法,使得通信内容变成乱码,双方需要预定义的通信秘钥和随机码才能解开.
对于安全的平台这种代码没有任何意义。
