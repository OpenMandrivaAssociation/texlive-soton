%global tl_name soton
%global tl_revision 16215

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	University of Southampton-compliant slides
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/soton
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/soton.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains two packages: soton-palette which defines colour-
ways, and soton-beamer, which uses the colours to produce compliant
presentations.

