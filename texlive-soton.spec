# revision 16215
# category Package
# catalog-ctan /macros/latex/contrib/soton
# catalog-date 2009-11-28 09:57:52 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-soton
Version:	0.1
Release:	8
Summary:	University of Southampton-compliant slides
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/soton
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 756076
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719557
- texlive-soton
- texlive-soton
- texlive-soton
- texlive-soton

