import os
import re
import shutil
import gzip
import zipfile
import sys
import hashlib

file_hashes = {
    'weather_Altdorf.npy': ('3d0d5b50308e4fcd3de8758a268221af', '76e3910e8a26ae7e5f30d7324ef80035284abadd'),
    'weather_Andermatt.npy': ('7a99d0966760ca4af3a7df1d2f0adfd6', '36f7c437cf2d1df1a093c9a483eadc9f2a23a8b6'),
    'weather_BaselBinningen.npy': ('dcddaf3f3ccf0db42782292ef479c98d', 'd09da8a19b35d5efc615c284244a3f180ed30ef5'),
    'weather_BernZollikofen.npy': ('baf6cbfaa6fbbf02fb5640e4d8a2e591', '15c847e50b910e9060b662432192f53690bde77b'),
    'weather_LaChaux_deFonds.npy': ('7a62cb95bcd929c08f53348cd208da3e', 'aabbdf4eb57c6cccf01165404d641dc6ff8484e9'),
    'weather_Chateau_dOex.npy': ('ab7be72c644fd74a5c303d03858d7a8b', '6bab6be4d03ceec2f8157ff3472d983976b48279'),
    'weather_Chaumont.npy': ('d1cd3d429da0fcf637f5a52d88416cc6', 'fad7e8166ca7564510307095ae654d42ef33bfae'),
    'weather_Davos.npy': ('9055774418731c3c091ce9111ed5fc2b', '7275264f87f1d349d213a7e6ea56d47d529f89ce'),
    'weather_Elm.npy': ('c817dd02f0bd5ec025cbcec1c3a875b9', '2ce5352cf4501284f47dc2ebb28be88afc5b5dd1'),
    'weather_Engelberg.npy': ('b390f9b07af1b204b0d61157d0697081', 'd0e4a6a15638316bd128578f97603896e04cfdc2'),
    'weather_Graechen.npy': ('8df5b62bee5b1103e36441e2f2c29d56', '9d7cbfefb494636e66ade57e132a4736b099089b'),
    'weather_GrimselHospiz.npy': ('01ee045015a162bd0cdf31f56dbcf416', '22082a59659736a3e025b1783c21c9d57cbfd73b'),
    'weather_Col_duGrandStBernard.npy': ('30cf4d6fd55af4010c0f9635e795c022', 'dd3981597a0d6538616f9e44fa33bb89826390c9'),
    'weather_GeneveCointrin.npy': ('555aef81deafa59ebc28c5f855bf8eb4', '04f2af7782e06dcebf559c316649947fa297d903'),
    'weather_Jungfraujoch.npy': ('cf4272cee337f2ce1bbe2b122e946656', 'f3d0135ea41560bffdd56c4dfc771fdc86fc224a'),
    'weather_Lugano.npy': ('dabdbc0a03b314147e4daec279350d90', '2cbf251bf14f708466dc5504f6ad72f0490773a9'),
    'weather_Luzern.npy': ('d5c3a0efc4ece56ceaee16de32240624', '9a45b1880d7354d0c227262a8b3774438e86712d'),
    'weather_Meiringen.npy': ('8b73cf8b76b8f399ddcc5a2f3662a616', 'd4ed3e2948ac86d2e10e29ca2825b84324311b6c'),
    'weather_Neuchatel.npy': ('98b0da4568ca89a99e5c6f4151f8a643', '09dff666777be20b0a3f347351701c69975c36fe'),
    'weather_LocarnoMonti.npy': ('52342db44182ce9f49c602aa7b13d60c', '05fc8e3a7eb81781856435097d92bdea9f010a65'),
    'weather_Payerne.npy': ('19c756e2ddb76dcb7b0d5de1bd9a21d0', '06967e092fe5ce7d12a27a15d194a520a71caae1'),
    'weather_BadRagaz.npy': ('f43b32cf3cf002a702cfe03e99a5aa1f', '7a707776380db81d77313a4123a97bd183d888de'),
    'weather_Saentis.npy': ('b12bc9e74ee66909d6e276e309849318', '31f6453eaf19a3ba270e522d73b3457ced085ec9'),
    'weather_Samedan.npy': ('e8f8746aa5b36c57a4c987885c31d537', 'ddbae814aea7bf8e3ce8b1056f4f537ad5fa2d6e'),
    'weather_StBernardino.npy': ('c78a67a3d9739367d5f6ae90595e33a5', 'f101f7f0d746e23f2a973a553e61e98abcaa82f9'),
    'weather_Segl-Maria.npy': ('b63c27e10eca9ffa3fc5a64ced184dd3', '725b965f2934ff353dccf749581f6ef3fffb55ed'),
    'weather_Sion.npy': ('b7d1ab7af56044c45b2a7afbd50ceaf6', 'eb3ee00e0466fba17b9b3e41f9a8870047def60c'),
    'weather_ZurichFluntern.npy': ('2ba9a3e089c61a7bd77aea73ee83ae8c', 'e65a2d2fd83bda765419016e395784d4a644feee'),
    'weather_StGallen.npy': ('1dd903e0f0f2785a9dbe96557c99bf3a', 'df78812adee670527fa7bf521a4580cbd13dc1b7')
}

BUF_SIZE = 65536
def hash_file(path):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
    return (md5.hexdigest(), sha1.hexdigest())

workDir = os.path.join(os.path.dirname(os.path.abspath(__file__)))

matcher = re.compile(r'(.+\.npy)\.gz')
with zipfile.ZipFile(os.path.join(workDir, 'data.zip'), mode='r') as zip_file:
    for filename in zip_file.namelist():
        match = matcher.match(filename)
        if not match is None:
            filepart = match.group(1)
            print("Unpacking... {}".format(filename),
                  end=(' ' * 50) + '\r')
            data = zip_file.read(filename)
            with open(os.path.join(workDir, filepart), mode='wb') as f_out:
                f_out.write(gzip.decompress(data))
            
            if filepart in file_hashes:
                if file_hashes[filepart] != hash_file(filepart):
                    print('Error MD5 or SHA1 hash does not match for file \'{}\'', filepart)
            else:
                print('Error hash not found for file \'{}\'', filepart)

print('Finished' + (' ' * 50))