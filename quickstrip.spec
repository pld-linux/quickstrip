Summary:	An Alpha tool for removing debugging information from kernel images
Summary(pl):	Narzêdzie do usuwania informacji debuggera z obrazów j±dra dla procesora Alpha
Name:		quickstrip
Version:	1.1
Release:	6
License:	distributable
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	%{name}-%{version}.tar.gz
ExclusiveArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quickstrip utility strips symbolic debugging information from
Linux/Alpha ECOFF binaries. The standard strip utility has occasional
problems with ECOFF binaries (especially, for example, with kernel
images), so quickstrip is used instead.

%description -l pl
Narzêdzie quickstrip usuwa informacje o symbolach dla debuggera z
binariów Linux/Alpha ECOFF. Standadowe narzêdzie strip miewa problemy
z binarkami ECOFF (zw³aszcza, na przyk³ad, obrazami kernela), wiêc
zamiast tego u¿ywa siê quickstrip.

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
