import os
import urllib.request

# Data from: https://www.ngdc.noaa.gov/stp/solar/solarflares.html

base_url = 'https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-features/solar-flares/x-rays/goes/xrs/'
urls = [
    'goes-xrs-report_1975.txt',
    'goes-xrs-report_1976.txt',
    'goes-xrs-report_1977.txt',
    'goes-xrs-report_1978.txt',
    'goes-xrs-report_1979.txt',
    'goes-xrs-report_1980.txt',
    'goes-xrs-report_1981.txt',
    'goes-xrs-report_1982.txt',
    'goes-xrs-report_1983.txt',
    'goes-xrs-report_1984.txt',
    'goes-xrs-report_1985.txt',
    'goes-xrs-report_1986.txt',
    'goes-xrs-report_1987.txt',
    'goes-xrs-report_1988.txt',
    'goes-xrs-report_1989.txt',
    'goes-xrs-report_1990.txt',
    'goes-xrs-report_1991.txt',
    'goes-xrs-report_1992.txt',
    'goes-xrs-report_1993.txt',
    'goes-xrs-report_1994.txt',
    'goes-xrs-report_1995.txt',
    'goes-xrs-report_1996.txt',
    'goes-xrs-report_1997.txt',
    'goes-xrs-report_1998.txt',
    'goes-xrs-report_1999.txt',
    'goes-xrs-report_2000.txt',
    'goes-xrs-report_2001.txt',
    'goes-xrs-report_2002.txt',
    'goes-xrs-report_2003.txt',
    'goes-xrs-report_2004.txt',
    'goes-xrs-report_2005.txt',
    'goes-xrs-report_2006.txt',
    'goes-xrs-report_2007.txt',
    'goes-xrs-report_2008.txt',
    'goes-xrs-report_2009.txt',
    'goes-xrs-report_2010.txt',
    'goes-xrs-report_2011.txt',
    'goes-xrs-report_2012.txt',
    'goes-xrs-report_2013.txt',
    'goes-xrs-report_2014.txt',
    'goes-xrs-report_2015.txt',
    'goes-xrs-report_2015_modifiedreplacedmissingrows.txt',
    'goes-xrs-report_2016.txt',
    'goes-xrs-report_2017-ytd.txt'
]

def downloadFile(url, fileName):
    if os.path.isfile(fileName):
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

for i, f in enumerate(urls):
    num = i + 1
    url = base_url + f
    print("Downloading... {}/{} ({:.2}) [{}%]".format(num, len(urls), num / len(urls) * 100, url))
    downloadFile(url, f)
    os.system("clear")
print("Finished.")