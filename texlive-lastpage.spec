# revision 23793
# category Package
# catalog-ctan /macros/latex/contrib/lastpage
# catalog-date 2011-09-01 15:02:59 +0200
# catalog-license gpl2
# catalog-version 1.2k
Name:		texlive-lastpage
Version:	1.2k
Release:	1
Summary:	Reference last page for Page N of M type footers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lastpage
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Reference the number of pages in your LaTeX document through
the introduction of a new label which can be referenced like
\pageref{LastPage} to give a reference to the last page of a
document. It is particularly useful in the page footer that
says: Page N of M.

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
%{_texmfdistdir}/tex/latex/lastpage/lastpage.sty
%{_texmfdistdir}/tex/latex/lastpage/lastpage209.sty
%doc %{_texmfdistdir}/doc/latex/lastpage/README
%doc %{_texmfdistdir}/doc/latex/lastpage/lastpage-example.pdf
%doc %{_texmfdistdir}/doc/latex/lastpage/lastpage-example.tex
%doc %{_texmfdistdir}/doc/latex/lastpage/lastpage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lastpage/lastpage.drv
%doc %{_texmfdistdir}/source/latex/lastpage/lastpage.dtx
%doc %{_texmfdistdir}/source/latex/lastpage/lastpage.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
