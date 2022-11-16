Name:		texlive-texsurgery
Version:	59885
Release:	1
Summary:	A LaTeX companion to the "texsurgery" python project
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texsurgery
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texsurgery.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texsurgery.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX library is a companion to the texsurgery python
project. It will make sure that "pdflatex document.tex" will
work, with reasonable defaults, for a document that is intended
to work with texsurgery, and also has other uses, always in
tandem with the texsurgery pypi package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/texsurgery
%doc %{_texmfdistdir}/doc/latex/texsurgery

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
