import os
from firebase_admin import credentials, initialize_app, storage


def retrive(folder):
    folder_path = f'{folder}/'  # Replace with your folder's path in Firebase Storage
    local_download_path = f'ByApp/{folder}/'  # Replace with the desired local path for downloaded files

# Create the local download folder if it doesn't exist
    if not os.path.exists(local_download_path):
        os.makedirs(local_download_path)

    blobs = bucket.list_blobs(prefix=folder_path)

    for blob in blobs:
    # Extract the file name from the full path
        file_name = os.path.basename(blob.name)
    
    # Construct the local file path
        local_file_path = os.path.join(local_download_path, file_name)

    # Download the file
        blob.download_to_filename(local_file_path)
    

characters_list = [
    "क (ka)",
    "ख (kha)",
    "ग (ga)",
    "घ (gha)",
    "ङ (nga)",
    "च (cha)",
    "छ (chha)",
    "ज (ja)",
    "झ (jha)",
    "ञ (nya)",
    "ट (ṭa)",
    "ठ (ṭha)",
    "ड (ḍa)",
    "ढ (ḍha)",
    "ण (ṇa)",
    "त (ta)",
    "थ (tha)",
    "द (da)",
    "ध (dha)",
    "न (na)",
    "प (pa)",
    "फ (pha)",
    "ब (ba)",
    "भ (bha)",
    "म (ma)",
    "य (ya)",
    "र (ra)",
    "ल (la)",
    "व (va)",
    "श (sha)",
    "ष (ṣa)",
    "स (sa)",
    "ह (ha)",
    "ष (ṣa)",
    "त्र (tra)",
    "क्‍ (adha k)",
    "ख्‍ (adha kha)",
    "ग्‍ (adha ga)",
    "घ्‍ (adha gha)",
    "च्‍ (adha cha)",
    "छ्‍(adha jh)",
    "ज्‍ (adha nya)",
    "झ्‍ (adha jh)",
    "ञ्‍ (adha jh)",
    "त्‍ (adha ta)",
    "थ्‍ (adha tha)",
    "द् (adha da)",
    "ध्‍ (adha dha)",
    "न्‍ (adha na)",
    "प्‍ (adha pa)",
    "फ्‍ (adha fa)",
    "ब्‍  (adha ba)",
    "भ्‍  (adha bha)",
    "म्‍. (adha m)",
    "य्‍. (adha ya)",
    "ल्‍. (adha la)",
    "व्‍  (adha va)",
    "श्‍. (adha sh)",
    "ष्‍. (adha sha)",
    "स्‍. (adha sa)",
    "ह्‍ (adha ha)",
    "\\",
    "/",
    ".",
    ":",
    "(ँ)",
    "(ँ)",
    "ो (o)",
    "ौ (au)",
    "अ (a)",
    "इ (i)",
    "उ (u)",
    "ऊ (uu)",
    "ऐ (ae)",
    "ा (a)",
    "ू (bada u)",
    "ि (i)",
    "ी (ii)",
    "ु (chota u)",
    "े (e)",
    "ै (ai)"
]



# Replace with your downloaded JSON file path
cred = credentials.Certificate("C:\\Users\\Lenovo\\Desktop\\MiniProject\\detail.json")
initialize_app(cred, {'storageBucket': 'inkalankar.appspot.com'})  # Replace with your Firebase Storage bucket URL
bucket = storage.bucket()
lis = ["gha","ka","ga"]
for i in lis:
    retrive(i)


