<h1>人工智能助手</h1>
<p>适用于树莓派、TinkerBoard等边缘侧的人工智能应用，通过网页进行操作，简单易用，便捷高效</p>
<h2>功能概要</h2>
<ul>
<li>调用边缘侧或远程摄像头，将画面投送到浏览器页面上，并进行人脸检测</li>
<li>控制服务器远程关机，启停摄像头</li>
<li>实现风扇的温控自动调节</li>
</ul>
<h2>使用方法</h2>
<h3>软件安装</h3>
<p>首先安装系统，推荐Debian Buster with Python3.7</p>
<pre>
cd /opt
sudo git clone https://github.com/ZongXR/AI-assistant.git
sudo apt-get install -y libcblas-dev libhdf5-dev libatlas-base-dev
sudo pip3 install -i https://www.piwheels.org/simple/ --extra-index-url https://pypi.org/simple -r ./requirements.txt
</pre>
<h3>硬件安装</h3>
<a href="https://blog.bombox.org/2021-08-28/raspberrypi-autofan/" target="_blank"><img src="https://blog.bombox.org/images/post/raspberrypi/fan_wiring.png" alt="硬件安装示意图" width="500"></a><br />
<h3>启动方式</h3>
<pre>
sudo nohup python3 /opt/AI-assistant/app.py &
</pre>
<h2>更新日志</h2>
<table>
<tr>
<th>版本号</th><th>更新内容</th><th>更新日期</th>
</tr>
<tr>
<td>0.1.0.0</td><td>调用远程摄像头捕获画面; 解耦摄像头地址作为配置项; 新增若干工具栏按钮</td><td>2023年12月17日</td>
</tr>
<tr>
<td>0.1.1.0</td><td>新增人脸检测功能</td><td>2023年12月18日</td>
</tr>
<tr>
<td>0.1.1.1</td><td>端口改为80;&nbsp;打开页面后先初始化&nbsp;暂停/开始&nbsp;按钮，并定时更新;&nbsp;定时关机时间改为60分钟</td><td>2023年12月19日</td>
</tr>
<tr>
<td>0.1.1.2</td><td>修复前端页面css导致的背景图错位</td><td>2023年12月19日</td>
</tr>
<tr>
<td>0.1.1.3</td><td>定时关机时间设定为0分钟;&nbsp;关机后关闭当前标签页</td><td>2023年12月21日</td>
</tr>
<tr>
<td>0.2.0.0</td><td>实现温控风扇，并按照温度调节转速</td><td>2023年12月25日</td>
</tr>
<tr>
<td>0.2.0.1</td><td>fix some bugs</td><td>2023年12月25日</td>
</tr>
<tr>
<td>0.2.0.2</td><td>fix some bugs</td><td>2023年12月26日</td>
</tr>
<tr>
<td>0.2.0.3</td><td>fix some bugs</td><td>2023年12月29日</td>
</tr>
</table>