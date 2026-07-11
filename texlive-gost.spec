%global tl_name gost
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2l
Release:	%{tl_revision}.1
Summary:	BibTeX styles to format according to GOST
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/gost
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
BibTeX styles to format bibliographies in English, Russian or Ukrainian
according to GOST 7.0.5-2008 or GOST 7.1-2003. Both 8-bit and Unicode
(UTF-8) versions of each BibTeX style, in each case offering a choice of
sorted and unsorted. Further, a set of three styles (which do not
conform to current standards) are retained for backwards compatibility.

