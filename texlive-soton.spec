Name:		texlive-soton
Version:	16215
Release:	2
Summary:	University of Southampton-compliant slides
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/soton
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains two packages: soton-palette which defines
colour-ways, and soton-beamer, which uses the colours to
produce compliant presentations.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/soton/soton-beamer.sty
%{_texmfdistdir}/tex/latex/soton/soton-palette.sty
%doc %{_texmfdistdir}/doc/latex/soton/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
