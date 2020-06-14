import requests
import os

chunk_size=256

url="https://redirector.googlevideo.com/videoplayback?expire=1589207170&ei=YkS5XtDuEuTPmwfigoM4&ip=5.180.220.209&id=7a9ccbe799c7340c&itag=136&source=picasa&requiressl=yes&ttl=transient&susc=ph&mh=bt&mm=32&mn=sn-aigzrn7d&ms=su&mv=m&mvi=4&pl=25&sc=yes&app=fife&ratebypass=yes&mime=video/mp4&otfp=1&gir=yes&clen=86494995&lmt=1589147260172135&dur=1420.085&alr=true&cpn=Gyh9kHRQfPXzqzvi&mpd_version=5&mt=1589199858&sparams=expire,ei,ip,id,itag,source,requiressl,ttl,susc,app,ratebypass,mime,otfp,gir,clen,lmt,dur&sig=AOq0QJ8wRQIgCV7Jweo4lKk-WROCHDwijdn6BrVIbSEQypmd8ldNsFMCIQDv8SCL1ohX7qWeKZs99FHQtPX3Y6l6V-gcqW7Bov9PSw==&lsparams=mh,mm,mn,ms,mv,mvi,pl,sc&lsig=AG3C_xAwRAIgW9IXG8GQSjrBxZMekwVpH9Xb8FzBWy34ackUDP5CvVICIAQlpRfJNPkBx2EFPkz5kp4027iRMbc9_CzCC_kJjWeo&jparams=MTAzLjIxOS4xNjYuMTg4&upx=TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3Ni4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc2LjA=#betaHost&tr=2"
r=requests.get(url,stream=True)
with open("jay.mp4","wb") as f:
	for c in r.iter_content(chunk_size=chunk_size):
		f.write(c)

aud="https://redirector.googlevideo.com/videoplayback?expire=1589207170&ei=YkS5XtDuEuTPmwfigoM4&ip=5.180.220.209&id=7a9ccbe799c7340c&itag=140&source=picasa&requiressl=yes&ttl=transient&susc=ph&mh=bt&mm=32&mn=sn-aigzrn7d&ms=su&mv=m&mvi=4&pl=25&sc=yes&app=fife&ratebypass=yes&mime=audio/mp4&otfp=1&gir=yes&clen=22984010&lmt=1589147260162344&dur=1420.132&alr=true&cpn=Gyh9kHRQfPXzqzvi&mpd_version=5&mt=1589199858&sparams=expire,ei,ip,id,itag,source,requiressl,ttl,susc,app,ratebypass,mime,otfp,gir,clen,lmt,dur&sig=AOq0QJ8wRQIgXElXwM0dlJlOUT8MLh7KQnp_BatnPlnMP26xCo-d8vUCIQD-4m9ybCUdV_68_PidU5sHRWK2Yjb1K4x_lAEcB-PFgw==&lsparams=mh,mm,mn,ms,mv,mvi,pl,sc&lsig=AG3C_xAwRQIhAKg_rbMUcD16EBlOHLHZdu2Dw2xmxObbUbjuXeWnnVUWAiAooXUqKCumOKG_dXNEkCKDrdcF5teduetdC2znhpu_cw==&jparams=MTAzLjIxOS4xNjYuMTg4&upx=TW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0OyBydjo3Ni4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzc2LjA=#betaHost"

rr=requests.get(aud,stream=True)
with open("ja.mp3","wb") as f:
	for c in rr.iter_content(chunk_size=chunk_size):
		f.write(c)

cmd = 'ffmpeg -y -i ja.mp3  -r 30 -i jay.mp4  -filter:a aresample=async=1 -c:a flac -c:v copy av.mkv'
os.system(cmd)                                     # "Muxing Done
print('Muxing Done')

