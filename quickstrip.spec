Summary:	An Alpha tool for removing debugging information from kernel images
Name:		quickstrip
Version:	1.1
Release:	6
ExclusiveArch:	alpha
Copyright:	distributable
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	quickstrip-1.1.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The quickstrip utility strips symbolic debugging information from
Linux/Alpha ECOFF binaries. The standard strip utility has occasional
problems with ECOFF binaries (especially, for example, with kernel
images), so quickstrip is used instead.

%prep
%setup -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir},%{mandir}/man1}

%{__make} install
install -s quickstrip $RPM_BUILD_ROOT%{_bindir}/quickstrip
install quickstrip.1 $RPM_BUILD_ROOT%{_mandir}/man1/quickstrip.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quickstrip
%{_mandir}/man1/quickstrip.1
