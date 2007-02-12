Summary:	An Alpha tool for removing debugging information from kernel images
Summary(pl.UTF-8):	Narzędzie do usuwania informacji debuggera z obrazów jądra dla procesora Alpha
Name:		quickstrip
Version:	1.1
Release:	6
License:	distributable
Group:		Development/Tools
Source0:	%{name}-%{version}.tar.gz
ExclusiveArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quickstrip utility strips symbolic debugging information from
Linux/Alpha ECOFF binaries. The standard strip utility has occasional
problems with ECOFF binaries (especially, for example, with kernel
images), so quickstrip is used instead.

%description -l pl.UTF-8
Narzędzie quickstrip usuwa informacje o symbolach dla debuggera z
binariów Linux/Alpha ECOFF. Standadowe narzędzie strip miewa problemy
z binarkami ECOFF (zwłaszcza, na przykład, obrazami kernela), więc
zamiast tego używa się quickstrip.

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
