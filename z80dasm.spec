Summary:	Z80 disassembler
Summary(pl.UTF-8):	Disasembler Z80
Name:		z80dasm
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://www.tablix.org/~avian/z80dasm/%{name}-%{version}.tar.gz
# Source0-md5:	d28fc8a3903ca253369ad723f5f88cf0
URL:		https://www.tablix.org/~avian/blog/articles/z80dasm/
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disassembler for the Zilog Z80 microprocessor and compatibles. It can
be used to reverse engineer programs and operating systems for 1980's
microcomputers using this processor architecture (for example Sinclar
ZX80, ZX81, Spectrum, Galaksija and others).

Generated assembly code can be assembled back with any of the
following:

zasm - Z80 assembler by Günter Woigk
z80asm - Available at http://savannah.nongnu.org/projects/z80asm/

or the original Zilog Z80 assembler.

z80dasm is based largely on dz80 3.0, written by Jan Panteltje
(available at http://panteltje.com/panteltje/z80/index.html). z80dasm
was extensively tested, a lot of bugs were fixed and a more UNIX-like
command line interface was added. See NEWS file for a summary of
changes.

%description -l pl.UTF-8
Disasembler dla procesora Z80 i kompatybilnych. Można go wykorzystać
do inżynierii wstecznej programów i systemów operacyjnych komputerów z
lat 80-tych XX wieku używających tej architektury procesora (np. ZX80,
ZX81, ZX Spectrum, Galaksija i inne).

Wygenerowany kod asemblerowy może być z powrotem zasemblowany przy
użyciu jednego z następujących programów:

zasm - asembler Z80 napisany przez Güntera Woigka
z80asm - udostępniony na http://savannah.nongnu.org/projects/z80asm/

lub oryginalnego asemblera Z80 Ziloga.

z80dasm bazuje w dużej mierze na dz80 3.0, napisanym przez Jana
Panteltje (kod dostępny pod adresem
http://panteltje.com/panteltje/z80/index.html). z80dasm był dobrze
przetestowany, wiele błędów zostało naprawionych i dodany został
interfejs linii poleceń w stylu uniksowym. Streszczenie zmian można
znaleźć w pliku NEWS.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/z80dasm
%{_mandir}/man1/z80dasm.1*
