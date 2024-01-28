def reverse_words(text):
    # Membagi teks menjadi kata-kata
    words = text.split()

    # Membalik urutan setiap kata dan membalik urutan huruf di dalam setiap kata
    reversed_words = [word[::-1] for word in words[::-1]]

    # Menggabungkan kata-kata yang telah dibalik kembali menjadi teks
    reversed_text = " ".join(reversed_words)

    return reversed_text
	
print(reverse_words('aku anak sehat'))