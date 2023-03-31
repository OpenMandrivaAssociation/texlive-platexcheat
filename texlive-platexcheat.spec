Name:		texlive-platexcheat
Version:	49557
Release:	2
Summary:	A LaTeX cheat sheet, in Japanese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/platexcheat
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platexcheat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/platexcheat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a translation to Japanese of Winston Chang's LaTeX
cheat sheet (a reference sheet for writing scientific papers).
It has been adapted to Japanese standards using pLaTeX, and
also attached additional information of "standard LaTeX"
(especially about math-mode).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/platexcheat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
