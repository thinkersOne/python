import urllib.request
import http.cookiejar;
import urllib.error;

###########request####################
# url = "http://tieba.baidu.com";
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8');#可在请求中设值 data请求参数，注：请求参数需要时 bytes类型
# headers = {
#     'User-Agent':'Mozilla/5.0(Windows NT6.1;Win64;x64)AppleWebKit/'
# };
# request = urllib.request.Request(url=url,headers=headers);#伪装浏览器方式请求，chrome
# # response = urllib.request.urlopen(url,timeout= 1,data=data);# 访问百度贴吧 并设值超时时间
# response = urllib.request.urlopen(request);
# html = response.read(); #获取到页面的源代码
# print(html.decode("utf-8"));#转化为utf-8编码

#########代理方式###################
# url = "http://tieba.baidu.com";
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8');#可在请求中设值 data请求参数，注：请求参数需要时 bytes类型
# headers = {
#     'User-Agent':'Mozilla/5.0(Windows NT6.1;Win64;x64)AppleWebKit/537.36'
#     '(KHTML,like Gecko)Chrome/56.0.2924.875Safari/537.36'
# };
# proxy_handler = urllib.request.ProxyHandler({
#     'http':'58.216.67.245:42017',
#     'https':'182.114.25.213:28801'
# })
# opener = urllib.request.build_opener(proxy_handler);
# urllib.request.install_opener(opener);
# request = urllib.request.Request(url=url,headers=headers);#伪装浏览器方式请求，chrome
# response = urllib.request.urlopen(request);
# html = response.read(); #获取到页面的源代码
# print(html.decode("utf-8"));#转化为utf-8编码

# 简单抓取百度贴吧 网页
# urllib 方式发起请求
# 代理ip提供商： http://http.zhiliandaili.cn/   http://www.etdaili.com

###########认证登录####################
# url = "http://tieba.baidu.com";
# user="lizhihao_life";
# password="b812w925";
# pwdmgr=urllib.request.HTTPPasswordMgrWithDefaultRealm();
# pwdmgr.add_password(None,url,user,password);
# auth_handler=urllib.request.HTTPBasicAuthHandler(pwdmgr);
# opener=urllib.request.build_opener(auth_handler);
# response = opener.open(url);
# html = response.read(); #获取到页面的源代码
# print(html.decode("utf-8"));#转化为utf-8编码

##########Cookie设值  并将cookie保存到cookie.txt文件中，该文件自动生成##########
# url = "http://tieba.baidu.com";
# fileName = 'cookie.txt';
# cookie = http.cookiejar.CookieJar();
# handler = urllib.request.HTTPCookieProcessor(cookie);
# opener=urllib.request.build_opener(handler);
# response = opener.open(url);
# f = open(fileName,'a');
# for item in cookie:
#     f.write(item.name+"="+item.value+"\n")
# f.close()
# print('----------------------------------------------------------------')
##########URLError  HTTPError##########
from urllib import request, error

url = "http://www.google.com";
try:
    response = request.urlopen(url)
except error.URLError as e:
    print('code:'+e.code+'\n')
# except error.HTTPError as e:
#     print('code:'+e.code+'\n')
#     print('reason:'+e.reason+'\n')
#     print('headers:'+e.headers+'\n')



