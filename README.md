# File-sharing-Bot




Telegram Bot untuk menyimpan Posting dan Dokumen dan dapat Diakses melalui Tautan Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang🔥
Terutama yang sagapung. 


### Fitur :

- Dapat disesuaikan sepenuhnya.
- Pesan sambutan & Forcesub yang dapat disesuaikan.
- Lebih dari satu Posting dalam Satu Tautan.
- Dapat digunakan di heroku secara langsung.

### Cara aktifkan bot :

- Tambahkan bot ke Saluran Basis Data dengan semua izin
- Tambahkan bot ke saluran ForceSub sebagai Admin dengan Undang Pengguna melalui Izin Tautan jika Anda mengaktifkan ForceSub 

##
### Installation
#### Deploy di Heroku
**SEBELUM ANDA DEPLOY DI HEROKU, ANDA HARUS FORK REPO INI DAN MENGUBAH NAMANYA KE YANG LAIN**<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)</br>


#### Deploy in your VPS
````bash
git clone https://github.com/Rexashh/File-Sharing-Xa
````
````bash
cd File-Sharing-Xa
````
````bash
pip3 install -r requirements.txt
````
````bash
nano sample.env
# Isi Data mu setelah selesai ganti nama :
````
````bash
cp sample.env .env
````
````bash
python3 main.py
````

### Perintah Admin

/start - mulai bot atau dapatkan postingan
/batch - buat tautan untuk lebih dari satu posting
/genlink - buat tautan untuk satu posting
/users - lihat statistik bot
/broadcast - menyiarkan pesan apa pun ke pengguna bot

### Vars yang tersedia

* `API_HASH` Hash API Anda dari my.telegram.org
* `API_ID` ID API Anda dari my.telegram.org
* `TG_BOT_TOKEN` Token bot Anda dari @BotFather
* `OWNER_ID` Harus memasukkan Id Telegram Anda
* `CHANNEL_ID` ID Saluran Anda, misalnya:- -100xxxxxxxx
* `ADMINS` Opsional: Daftar user_id Admin yang dipisahkan spasi, mereka hanya dapat membuat tautan
* `START_MESSAGE` Opsional: mulai pesan bot, gunakan HTML dan <a href='https://github.com/Rexashh/onebuttonfiles-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Opsional: Paksa sub pesan bot, gunakan HTML dan Isi
* `FORCE_SUB_CHANNEL` Opsional: ID Saluran ForceSub, biarkan 0 jika Anda ingin menonaktifkan sub paksa
* `PROTECT_CONTENT` Isi: True jika Anda perlu mencegah penerusan file

### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/CodeXBotz/File-Sharing-Bot/blob/main/README.md#custom_caption'>fillings</a> for formatting (only for documents)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - Nama depan pengguna
* `{last}` - Nama belakang pengguna
* `{id}` - User ID
* `{mention}` - Sebutkan pengguna
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - nama file Dokumen
* `{previouscaption}` - Keterangan Asli


## Support   
[Group](https://t.me/rexaprivateroom) 
[Channel](https://t.me/tirexgugel) 
   
### Credits

- Thanks To Dan For His Awsome [Libary](https://github.com/pyrogram/pyrogram)
- Our Support Group Members
- Thanks to [CodeXBotz](https://github.com/CodeXBotz/File-Sharing-Bot/)

##

   **Star this Repo if you Liked it ⭐⭐⭐**

