Name:		texlive-lastpage
Version:	60414
Release:	2
Summary:	Reference last page for Page N of M type footers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lastpage
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Reference the number of pages in your LaTeX document through
the introduction of a new label which can be referenced like
\pageref{LastPage} to give a reference to the last page of a
document. It is particularly useful in the page footer that
says: Page N of M.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
