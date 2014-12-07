# revision 27642
# category Package
# catalog-ctan /biblio/bibtex/contrib/gost
# catalog-date 2012-09-10 13:53:05 +0200
# catalog-license lppl
# catalog-version 1.2a
Name:		texlive-gost
Epoch:		1
Version:	1.2a
Release:	8
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
BibTeX styles to format bibliographies in English, Russian or
Ukrainian according to GOST 7.0.5-2008 or GOST 7.1-2003. Both
8-bit and Unicode (UTF-8) versions of each BibTeX style, in
each case offering a choice of sorted and unsorted. Further, a
set of three styles (which do not conform to current standards)
are retained for backwards compatibility.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/gost/gost2003.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2003s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008l.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008ls.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008n.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008ns.bst
%{_texmfdistdir}/bibtex/bst/gost/gost2008s.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780.bst
%{_texmfdistdir}/bibtex/bst/gost/gost780s.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2003.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2003s.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008l.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008ls.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008n.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008ns.bst
%{_texmfdistdir}/bibtex/bst/gost/ugost2008s.bst
%{_texmfdistdir}/bibtex/csf/gost/cp1251.csf
%{_texmfdistdir}/bibtex/csf/gost/koi8u.csf
%{_texmfdistdir}/bibtex/csf/gost/ruscii.csf
%{_texmfdistdir}/bibtex/csf/gost/utf8cyrillic.csf
%doc %{_texmfdistdir}/doc/bibtex/gost/README
%doc %{_texmfdistdir}/doc/bibtex/gost/gost.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2003.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008-customized.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008-natbib-s.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008-natbib.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008-sorted.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008.pdf
%doc %{_texmfdistdir}/doc/bibtex/gost/gost2008l.pdf
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
