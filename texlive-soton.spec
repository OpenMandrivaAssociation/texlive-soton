# revision 16215
# category Package
# catalog-ctan /macros/latex/contrib/soton
# catalog-date 2009-11-28 09:57:52 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-soton
Version:	0.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
The bundle contains two packages: soton-palette which defines
colour-ways, and soton-beamer, which uses the colours to
produce compliant presentations.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/soton/soton-beamer.sty
%{_texmfdistdir}/tex/latex/soton/soton-palette.sty
%doc %{_texmfdistdir}/doc/latex/soton/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
