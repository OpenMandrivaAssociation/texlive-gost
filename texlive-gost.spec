# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/gost
# catalog-date 2007-01-04 14:33:27 +0100
# catalog-license lppl
# catalog-version 2005.08.12
Name:		texlive-gost
Version:	2005.08.12
Release:	1
Summary:	BibTeX styles to format according to GOST
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/gost
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gost.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
BibTeX styles to format bibliography in English, Russian and
Ukrainian according to GOST 7.1-84 and GOST 7.80-00.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/gost/gost71s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost71u.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780u.bst
%{_texmfdistdir}/bibtex/csf/gost/cp1251.csf
%{_texmfdistdir}/bibtex/csf/gost/koi8u.csf
%{_texmfdistdir}/bibtex/csf/gost/ruscii.csf
%doc %{_texmfdistdir}/doc/bibtex/gost/README
%doc %{_texmfdistdir}/doc/bibtex/gost/gost71.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost780.pdf
#- source
%doc %{_texmfdistdir}/source/bibtex/gost/gost.dtx
%doc %{_texmfdistdir}/source/bibtex/gost/gost.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
