import streamlit as st

def main():
    st.title("MY BIOGRAPHY")
    st.header("LIE ERALDO MANASON")
    st.image("Photo.jpg", width=300)

    st.subheader("Profil")
    st.write("Nama saya adalah Lie Eraldo Manason. Saya adalah seseorang yang memiliki semangat kerja yang tinggi, memiliki kemampuan untuk belajar hal-hal yang baru dengan sangat cepat, pekerja keras, disiplin, dan jujur. Saya yakin bahwa dengan kemampuan dan keterampilan yang saya miliki, saya dapat memberikan kontribusi yang sangat berarti bagi perusahaan anda")
    
    st.markdown("---")

    st.subheader("Detail Data Pribadi")
    st.write("**Tempat, Tanggal Lahir :**")
    st.write("Semarang, 29 Januari 2003")
    st.write("**Alamat :**")
    st.write("Jl. Tambak Mas X No. 123, Semarang, Jawa Tengah")
    st.write("**Jenis Kelamin :**")
    st.write("Laki-Laki")
    st.write("**Kewarganegaraan :**")
    st.write("Indonesia")
    st.write("**Tinggi Badan**")
    st.write("178")
    st.write("**Berat Badan**")
    st.write("80")

    st.subheader("Pendidikan")
    st.write("- 2006-2008   : TK Kanisius Hasanudin, Semarang")
    st.write("- 2008-2015   : SD Kanisius Hasanudin, Semarang")
    st.write("- 2015-2018   : SMP Kristen Terang Bangsa, Semarang")
    st.write("- 2018-2021   : SMA Kristen Terang Bangsa, Semarang")
    st.write("- 2022-sekarang : Universitas Nasional Karangturi, Semarang")

    st.subheader("Pengalaman Kerja") 
    st.write("- Juli 2019 : Youth Amplify Event Committe Menjadi Event Organizer")
    st.write("- Desember 2021 - Januari 2022 : Youth Real Love Event Committe Menjadi Guest Assistant")
    st.write("- September 2021 - September 2022 : Bekerja di RM.Kelengan Semarang")
    st.write("- Januari 2023 - sekarang : Usaha dibidang FnB")

    st.subheader("Kemampuan")
    st.write("- Komunikasi yang baik")
    st.write("- Kemampuan untuk mengorganisir dengan baik")
    st.write("- Pemahaman yang baik")
    st.write("- Dapat Diandalkan") 

    st.subheader("Keahlian")
    st.write("- Microsoft Word   5/5")
    st.write("- Microsoft Excel  4/5")
    st.write("- Microsoft Office 5/5")

    st.subheader("Contact Personal")
    st.info("Email : eraldo.matius@gmail.com")
    st.info("WhatsApp : 081225030660")
    st.info("Intagram : @eraldolie")
if __name__ == '__main__':
     main()
