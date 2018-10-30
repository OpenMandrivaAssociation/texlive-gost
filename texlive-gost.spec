Name:		texlive-gost
Epoch:		1
Version:	1.2i
Release:	2
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
%{_texmfdistdir}/bibtex/bst/gost
%{_texmfdistdir}/bibtex/csf/gost
%doc %{_texmfdistdir}/doc/bibtex/gost
#- source
%doc %{_texmfdistdir}/source/bibtex/gost

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc source %{buildroot}%{_texmfdistdir}
