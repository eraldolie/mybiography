import streamlit as st

def main():
    st.snow()
    st.title("MY BIOGRAPHY")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.image("photo.jpg", width=300)
    with col3:
        st.write('')


    st.subheader("Profil")
    st.write("Nama saya adalah Lie Eraldo Manason. Saya adalah seseorang yang memiliki semangat kerja yang tinggi, memiliki kemampuan untuk belajar hal-hal yang baru dengan sangat cepat, pekerja keras, disiplin, dan jujur. Saya yakin bahwa dengan kemampuan dan keterampilan yang saya miliki, saya dapat memberikan kontribusi yang sangat berarti bagi perusahaan anda")
    
    st.markdown("---")

    st.subheader("Detail Data Pribadi")
    st.text_input('**Nama Lengkap**',"Lie, Eraldo Manason")
    st.text_input('**Tempat, Tanggal Lahir**',"Semarang, 29 Januari 2003")
    st.text_input('**Alamat**', "Jl. Tambak Mas X No. 123, Semarang, Jawa Tengah")
    st.text_input('Jenis Kelamin',"Laki-Laki")
    st.text_input('**Kewarganegaraa**',"Indonesia")
    st.text_input('**Tinggi Badan**',"178")
    st.text_input('**Berat Badan**',"80")

    st.info(":pushpin: Pendidikan")
    st.write("- 2006-2008   : TK Kanisius Hasanudin, Semarang")
    st.write("- 2008-2015   : SD Kanisius Hasanudin, Semarang")
    st.write("- 2015-2018   : SMP Kristen Terang Bangsa, Semarang")
    st.write("- 2018-2021   : SMA Kristen Terang Bangsa, Semarang")
    st.write("- 2022-sekarang : Universitas Nasional Karangturi, Semarang")

    st.info(":pushpin: Pengalaman Kerja") 
    st.write("- Juli 2019 : Youth Amplify Event Committe Menjadi Event Organizer")
    st.write("- Desember 2021 - Januari 2022 : Youth Real Love Event Committe Menjadi Guest Assistant")
    st.write("- September 2021 - September 2022 : Bekerja di RM.Kelengan Semarang")
    st.write("- Januari 2023 - sekarang : Usaha dibidang FnB")

    col1, col2 = st.columns(2)
    with col1:
          st.info(":pushpin: Kemampuan")
          st.write("- Komunikasi yang baik")
          st.write("- Kemampuan untuk mengorganisir dengan baik")
          st.write("- Pemahaman yang baik")
          st.write("- Dapat Diandalkan") 
    with col2:
          st.info(":pushpin: Keahlian")
          st.write("- Microsoft Word   :five:")
          st.write("- Microsoft Excel  :four:")
          st.write("- Microsoft Office :five:")

    st.markdown("---")
    
    st.subheader(":arrow_forward: Contact Personal")
    st.info(':e-mail: eraldo.matius@gmail.com')
    st.info(':telephone_receiver: Call Number [whatsApp](https://wa.me/6281225030660)')
    st.info(':star: Social Media [Instagram](https://instagram.com/eraldolie)')
    
    st.subheader(":arrow_forward: Kritik Dan Saran")
    nama_pengguna = st.text_input("Masukkan Nama Anda")
    komentar = st.text_area("Masukkan Komentar Anda di sini")
    submitted = st.button("submit")
    if submitted:
        st.write("Nama :", nama_pengguna)
        st.write("Menanggapi :", komentar)


if __name__ == '__main__':
    main()
    
