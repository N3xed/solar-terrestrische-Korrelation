base_url = 'https://www.ncei.noaa.gov/data/solar-spectral-irradiance/access/daily/'
urls = [
    'ssi_v02r01_daily_s18820101_e18821231_c20170717.nc',
    'ssi_v02r01_daily_s18830101_e18831231_c20170717.nc',
    'ssi_v02r01_daily_s18840101_e18841231_c20170717.nc',
    'ssi_v02r01_daily_s18850101_e18851231_c20170717.nc',
    'ssi_v02r01_daily_s18860101_e18861231_c20170717.nc',
    'ssi_v02r01_daily_s18870101_e18871231_c20170717.nc',
    'ssi_v02r01_daily_s18880101_e18881231_c20170717.nc',
    'ssi_v02r01_daily_s18890101_e18891231_c20170717.nc',
    'ssi_v02r01_daily_s18900101_e18901231_c20170717.nc',
    'ssi_v02r01_daily_s18910101_e18911231_c20170717.nc',
    'ssi_v02r01_daily_s18920101_e18921231_c20170717.nc',
    'ssi_v02r01_daily_s18930101_e18931231_c20170717.nc',
    'ssi_v02r01_daily_s18940101_e18941231_c20170717.nc',
    'ssi_v02r01_daily_s18950101_e18951231_c20170717.nc',
    'ssi_v02r01_daily_s18960101_e18961231_c20170717.nc',
    'ssi_v02r01_daily_s18970101_e18971231_c20170717.nc',
    'ssi_v02r01_daily_s18980101_e18981231_c20170717.nc',
    'ssi_v02r01_daily_s18990101_e18991231_c20170717.nc',
    'ssi_v02r01_daily_s19000101_e19001231_c20170717.nc',
    'ssi_v02r01_daily_s19010101_e19011231_c20170717.nc',
    'ssi_v02r01_daily_s19020101_e19021231_c20170718.nc',
    'ssi_v02r01_daily_s19030101_e19031231_c20170718.nc',
    'ssi_v02r01_daily_s19040101_e19041231_c20170718.nc',
    'ssi_v02r01_daily_s19050101_e19051231_c20170718.nc',
    'ssi_v02r01_daily_s19060101_e19061231_c20170718.nc',
    'ssi_v02r01_daily_s19070101_e19071231_c20170718.nc',
    'ssi_v02r01_daily_s19080101_e19081231_c20170718.nc',
    'ssi_v02r01_daily_s19090101_e19091231_c20170718.nc',
    'ssi_v02r01_daily_s19100101_e19101231_c20170718.nc',
    'ssi_v02r01_daily_s19110101_e19111231_c20170718.nc',
    'ssi_v02r01_daily_s19120101_e19121231_c20170718.nc',
    'ssi_v02r01_daily_s19130101_e19131231_c20170718.nc',
    'ssi_v02r01_daily_s19140101_e19141231_c20170718.nc',
    'ssi_v02r01_daily_s19150101_e19151231_c20170718.nc',
    'ssi_v02r01_daily_s19160101_e19161231_c20170718.nc',
    'ssi_v02r01_daily_s19170101_e19171231_c20170718.nc',
    'ssi_v02r01_daily_s19180101_e19181231_c20170718.nc',
    'ssi_v02r01_daily_s19190101_e19191231_c20170718.nc',
    'ssi_v02r01_daily_s19200101_e19201231_c20170718.nc',
    'ssi_v02r01_daily_s19210101_e19211231_c20170718.nc',
    'ssi_v02r01_daily_s19220101_e19221231_c20170718.nc',
    'ssi_v02r01_daily_s19230101_e19231231_c20170718.nc',
    'ssi_v02r01_daily_s19240101_e19241231_c20170718.nc',
    'ssi_v02r01_daily_s19250101_e19251231_c20170718.nc',
    'ssi_v02r01_daily_s19260101_e19261231_c20170718.nc',
    'ssi_v02r01_daily_s19270101_e19271231_c20170718.nc',
    'ssi_v02r01_daily_s19280101_e19281231_c20170718.nc',
    'ssi_v02r01_daily_s19290101_e19291231_c20170718.nc',
    'ssi_v02r01_daily_s19300101_e19301231_c20170718.nc',
    'ssi_v02r01_daily_s19310101_e19311231_c20170718.nc',
    'ssi_v02r01_daily_s19320101_e19321231_c20170718.nc',
    'ssi_v02r01_daily_s19330101_e19331231_c20170718.nc',
    'ssi_v02r01_daily_s19340101_e19341231_c20170718.nc',
    'ssi_v02r01_daily_s19350101_e19351231_c20170718.nc',
    'ssi_v02r01_daily_s19360101_e19361231_c20170718.nc',
    'ssi_v02r01_daily_s19370101_e19371231_c20170718.nc',
    'ssi_v02r01_daily_s19380101_e19381231_c20170718.nc',
    'ssi_v02r01_daily_s19390101_e19391231_c20170718.nc',
    'ssi_v02r01_daily_s19400101_e19401231_c20170718.nc',
    'ssi_v02r01_daily_s19410101_e19411231_c20170718.nc',
    'ssi_v02r01_daily_s19420101_e19421231_c20170718.nc',
    'ssi_v02r01_daily_s19430101_e19431231_c20170718.nc',
    'ssi_v02r01_daily_s19440101_e19441231_c20170718.nc',
    'ssi_v02r01_daily_s19450101_e19451231_c20170718.nc',
    'ssi_v02r01_daily_s19460101_e19461231_c20170718.nc',
    'ssi_v02r01_daily_s19470101_e19471231_c20170718.nc',
    'ssi_v02r01_daily_s19480101_e19481231_c20170718.nc',
    'ssi_v02r01_daily_s19490101_e19491231_c20170718.nc',
    'ssi_v02r01_daily_s19500101_e19501231_c20170717.nc',
    'ssi_v02r01_daily_s19510101_e19511231_c20170717.nc',
    'ssi_v02r01_daily_s19520101_e19521231_c20170717.nc',
    'ssi_v02r01_daily_s19530101_e19531231_c20170717.nc',
    'ssi_v02r01_daily_s19540101_e19541231_c20170717.nc',
    'ssi_v02r01_daily_s19550101_e19551231_c20170717.nc',
    'ssi_v02r01_daily_s19560101_e19561231_c20170717.nc',
    'ssi_v02r01_daily_s19570101_e19571231_c20170717.nc',
    'ssi_v02r01_daily_s19580101_e19581231_c20170717.nc',
    'ssi_v02r01_daily_s19590101_e19591231_c20170717.nc',
    'ssi_v02r01_daily_s19600101_e19601231_c20170717.nc',
    'ssi_v02r01_daily_s19610101_e19611231_c20170717.nc',
    'ssi_v02r01_daily_s19620101_e19621231_c20170717.nc',
    'ssi_v02r01_daily_s19630101_e19631231_c20170717.nc',
    'ssi_v02r01_daily_s19640101_e19641231_c20170717.nc',
    'ssi_v02r01_daily_s19650101_e19651231_c20170717.nc',
    'ssi_v02r01_daily_s19660101_e19661231_c20170717.nc',
    'ssi_v02r01_daily_s19670101_e19671231_c20170717.nc',
    'ssi_v02r01_daily_s19680101_e19681231_c20170717.nc',
    'ssi_v02r01_daily_s19690101_e19691231_c20170717.nc',
    'ssi_v02r01_daily_s19700101_e19701231_c20170718.nc',
    'ssi_v02r01_daily_s19710101_e19711231_c20170718.nc',
    'ssi_v02r01_daily_s19720101_e19721231_c20170718.nc',
    'ssi_v02r01_daily_s19730101_e19731231_c20170718.nc',
    'ssi_v02r01_daily_s19740101_e19741231_c20170718.nc',
    'ssi_v02r01_daily_s19750101_e19751231_c20170718.nc',
    'ssi_v02r01_daily_s19760101_e19761231_c20170718.nc',
    'ssi_v02r01_daily_s19770101_e19771231_c20170718.nc',
    'ssi_v02r01_daily_s19780101_e19781231_c20170718.nc',
    'ssi_v02r01_daily_s19790101_e19791231_c20170718.nc',
    'ssi_v02r01_daily_s19800101_e19801231_c20170718.nc',
    'ssi_v02r01_daily_s19810101_e19811231_c20170718.nc',
    'ssi_v02r01_daily_s19820101_e19821231_c20170718.nc',
    'ssi_v02r01_daily_s19830101_e19831231_c20170718.nc',
    'ssi_v02r01_daily_s19840101_e19841231_c20170718.nc',
    'ssi_v02r01_daily_s19850101_e19851231_c20170718.nc',
    'ssi_v02r01_daily_s19860101_e19861231_c20170718.nc',
    'ssi_v02r01_daily_s19870101_e19871231_c20170718.nc',
    'ssi_v02r01_daily_s19880101_e19881231_c20170718.nc',
    'ssi_v02r01_daily_s19890101_e19891231_c20170718.nc',
    'ssi_v02r01_daily_s19900101_e19901231_c20170718.nc',
    'ssi_v02r01_daily_s19910101_e19911231_c20170718.nc',
    'ssi_v02r01_daily_s19920101_e19921231_c20170718.nc',
    'ssi_v02r01_daily_s19930101_e19931231_c20170718.nc',
    'ssi_v02r01_daily_s19940101_e19941231_c20170718.nc',
    'ssi_v02r01_daily_s19950101_e19951231_c20170718.nc',
    'ssi_v02r01_daily_s19960101_e19961231_c20170718.nc',
    'ssi_v02r01_daily_s19970101_e19971231_c20170718.nc',
    'ssi_v02r01_daily_s19980101_e19981231_c20170718.nc',
    'ssi_v02r01_daily_s19990101_e19991231_c20170718.nc',
    'ssi_v02r01_daily_s20000101_e20001231_c20170718.nc',
    'ssi_v02r01_daily_s20010101_e20011231_c20170718.nc',
    'ssi_v02r01_daily_s20020101_e20021231_c20170718.nc',
    'ssi_v02r01_daily_s20030101_e20031231_c20170718.nc',
    'ssi_v02r01_daily_s20040101_e20041231_c20170718.nc',
    'ssi_v02r01_daily_s20050101_e20051231_c20170718.nc',
    'ssi_v02r01_daily_s20060101_e20061231_c20170718.nc',
    'ssi_v02r01_daily_s20070101_e20071231_c20170718.nc',
    'ssi_v02r01_daily_s20080101_e20081231_c20170718.nc',
    'ssi_v02r01_daily_s20090101_e20091231_c20170718.nc',
    'ssi_v02r01_daily_s20100101_e20101231_c20170718.nc',
    'ssi_v02r01_daily_s20110101_e20111231_c20170718.nc',
    'ssi_v02r01_daily_s20120101_e20121231_c20170718.nc',
    'ssi_v02r01_daily_s20130101_e20131231_c20170718.nc',
    'ssi_v02r01_daily_s20140101_e20141231_c20170718.nc',
    'ssi_v02r01_daily_s20150101_e20151231_c20170718.nc',
    'ssi_v02r01_daily_s20160101_e20161231_c20170718.nc',
    'ssi_v02r01_daily_s20170101_e20171231_c20180227.nc',
    'ssi_v02r01_daily_s20180101_e20181231_c20190409.nc'
]

import os
import urllib.request

def downloadFile(url, fileName):
    if os.path.isfile(fileName):
        print("Skipping file '{}': already exists.", fileName)
        return
    with urllib.request.urlopen(url) as u:
        with open(fileName, 'wb') as f:
            contentLen = u.headers['content-length']
            try:
                contentLen = int(contentLen)
            except():
                contentLen = 0
            print("Downloading '{0}' to '{1}'".format(url.split("/")[-1], fileName), " ({0} bytes)".format(contentLen) if contentLen > 0 else "")
            dlCount = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    print()
                    break
                dlCount += len(buffer)
                f.write(buffer)
                print("%10d  [%3.2f%%]" % (dlCount, dlCount * 100. / contentLen), end="\r")

for i, filename in enumerate(urls):
    num = i + 1
    url = base_url + filename
    print("Downloading... {}/{} ({:.2}) [{}]".format(num, len(urls), num / len(urls) * 100, url))
    file_path = url.split('/')[-1]
    downloadFile(url, file_path)
    os.system("clear")
print("Finished.")
