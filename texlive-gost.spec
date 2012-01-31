# revision 25194
# category Package
# catalog-ctan /biblio/bibtex/contrib/gost
# catalog-date 2012-01-25 00:32:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-gost
Version:	20120125
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
Ukrainian according to GOST 7.0.5-2008, GOST 7.1-2003, GOST
7.80-2000 and GOST 7.11-2004. Both 8-bit and Unicode (UTF-8)
versions of each BibTeX style, in each case offering a choice
of sorted and unsorted. Further, a set of three styles (which
do not conform to current standards) are retained for backwards
compatibility.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/gost/gost705s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost705u.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780u.bst
%{_texmfdistdir}/bibtex/bst/gost/unicode-gost705s.bst
%{_texmfdistdir}/bibtex/bst/gost/unicode-gost705u.bst
%{_texmfdistdir}/bibtex/bst/gost/unicode-gost780s.bst
%{_texmfdistdir}/bibtex/bst/gost/unicode-gost780u.bst
%{_texmfdistdir}/bibtex/csf/gost/cp1251.csf
%{_texmfdistdir}/bibtex/csf/gost/koi8u.csf
%{_texmfdistdir}/bibtex/csf/gost/ruscii.csf
%{_texmfdistdir}/bibtex/csf/gost/utf8cyrillic.csf
%doc %{_texmfdistdir}/doc/bibtex/gost/README
%doc %{_texmfdistdir}/doc/bibtex/gost/gost705-custom.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost705-sorted.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost705-unsorted.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost705.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost780.pdf
#- source
%doc %{_texmfdistdir}/source/bibtex/gost/gost.dtx
%doc %{_texmfdistdir}/source/bibtex/gost/gost.ins
%doc %{_texmfdistdir}/source/bibtex/gost/unicode-gost.dtx
%doc %{_texmfdistdir}/source/bibtex/gost/unicode-gost.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
