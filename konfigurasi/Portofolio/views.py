from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def Certification(request):
    certs = [
        {
            "title": "BNSP: Pengembang Web Pratama (Junior Web Developer)",
            "issuer": "BNSP / LSP BPPTIK",
            "date": "24 Nov 2025",
            "desc": "Sertifikat kompetensi bidang Pemrograman dan Pengembangan Perangkat Lunak. Berlaku 3 tahun, mencakup 6 unit kompetensi.",
            "icon": "bi-patch-check",
            "image": "images/Certificate_BNSP1 copy.jpeg",
        },
        {
            "title": "Coding Camp powered by DBS Foundation: Machine Learning Engineer",
            "issuer": "Dicoding x DBS Foundation",
            "date": "7 Jul 2025",
            "desc": "Dinyatakan lulus program Coding Camp periode 10 Feb - 16 Jul 2025, spesialisasi Machine Learning Engineer.",
            "icon": "bi-mortarboard",
            "image": "images/Screenshot 2026-10-02 at 01.44.32.png",
        },
        {
            "title": "Certificate of Achievement: Capstone Project",
            "issuer": "Dicoding x DBS Foundation",
            "date": "7 Jul 2025",
            "desc": "Terpilih sebagai salah satu dari 20 tim terbaik pada Capstone Project Coding Camp 2025.",
            "icon": "bi-trophy",
            "image": "images/[Coding Camp 2025 - University] Best Capstone Project - MC211D5Y2136 copy.jpg",
        },
        {
            "title": "Studi Independen Bersertifikat (MSIB) Angkatan 7: AI4JOBS",
            "issuer": "Kampus Merdeka x PT Orbit Ventura Indonesia",
            "date": "31 Des 2024",
            "desc": "Program AI4JOBS 6 Sep - 31 Des 2024 dengan total 900 jam belajar.",
            "icon": "bi-award",
            "image": "images/orbit.png",
        },
        {
            "title": "Certificate of Appreciation: Orbit Jobs Fair 2024",
            "issuer": "Orbit Future Academy",
            "date": "12 Des 2024",
            "desc": "Partisipasi dalam Orbit Jobs Fair 2024, Jakarta.",
            "icon": "bi-star",
            "image": "images/Roby Saidi Prasetyo copy.jpg",
        },
    ]
    return render(request, 'Certification.html', {"certs": certs})
def kontak(request):
    return render(request, 'kontak.html')

def resume(request):
    return render(request, 'resume.html')