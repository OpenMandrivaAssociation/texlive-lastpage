%global tl_name lastpage
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1h
Release:	%{tl_revision}.1
Summary:	Reference last page for Page N of M type footers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lastpage
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lastpage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Reference the number of pages in your LaTeX document through the
introduction of a new label which can be referenced like
\pageref{LastPage} to give a reference to the last page of a document.
It is particularly useful in the page footer that says: Page N of M.

