Summary:	An Alpha tool for removing debugging information from kernel images
Summary(pl):	Narz�dzie do usuwania informacji debuggera z obraz�w j�dra dla procesora Alpha
Name:		quickstrip
Version:	1.1
Release:	6
License:	distributable
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	%{name}-%{version}.tar.gz
ExclusiveArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quickstrip utility strips symbolic debugging information from
Linux/Alpha ECOFF binaries. The standard strip utility has occasional
problems with ECOFF binaries (especially, for example, with kernel
images), so quickstrip is used instead.

%description -l pl
Narz�dzie quickstrip usuwa informacje o symbolach dla debuggera z
binari�w Linux/Alpha ECOFF. Standadowe narz�dzie strip miewa problemy
z binarkami ECOFF (zw�aszcza, na przyk�ad, obrazami kernela), wi�c
zamiast tego u�ywa si� quickstrip.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir},%{mandir}/man1}

%{__make} install
install quickstrip $RPM_BUILD_ROOT%{_bindir}/quickstrip
install quickstrip.1 $RPM_BUILD_ROOT%{_mandir}/man1/quickstrip.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quickstrip
%{_mandir}/man1/quickstrip.1*
