#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : compat-iptables-soname0.1.0
Version  : 1.8.2
Release  : 6
URL      : https://www.netfilter.org/projects/iptables/files/iptables-1.8.2.tar.bz2
Source0  : https://www.netfilter.org/projects/iptables/files/iptables-1.8.2.tar.bz2
Source1 : https://www.netfilter.org/projects/iptables/files/iptables-1.8.2.tar.bz2.sig
Summary  : Shared Xtables code for extensions and iproute2
Group    : Development/Tools
License  : GPL-2.0
Requires: compat-iptables-soname0.1.0-lib = %{version}-%{release}
Requires: compat-iptables-soname0.1.0-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : pkgconfig(libmnl)
BuildRequires : pkgconfig(libnetfilter_conntrack)
BuildRequires : pkgconfig(libnfnetlink)
BuildRequires : pkgconfig(libnftnl)
# Suppress generation of debuginfo
%global debug_package %{nil}
Patch1: cve-2012-2663.patch
Patch2: cve-2019-11360.patch

%description
No detailed description available

%package lib
Summary: lib components for the compat-iptables-soname0.1.0 package.
Group: Libraries
Requires: compat-iptables-soname0.1.0-license = %{version}-%{release}

%description lib
lib components for the compat-iptables-soname0.1.0 package.


%package license
Summary: license components for the compat-iptables-soname0.1.0 package.
Group: Default

%description license
license components for the compat-iptables-soname0.1.0 package.


%prep
%setup -q -n iptables-1.8.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1567812517
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-devel --enable-ipv6
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1567812517
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/compat-iptables-soname0.1.0
cp COPYING %{buildroot}/usr/share/package-licenses/compat-iptables-soname0.1.0/COPYING
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/lib64/libiptc.so.0
rm -f %{buildroot}/usr/lib64/libiptc.so.0.0.0
rm -f %{buildroot}/usr/lib64/libxtables.so.12
rm -f %{buildroot}/usr/lib64/libxtables.so.12.2.0
rm -f %{buildroot}/usr/bin/arptables
rm -f %{buildroot}/usr/bin/arptables-nft
rm -f %{buildroot}/usr/bin/arptables-nft-restore
rm -f %{buildroot}/usr/bin/arptables-nft-save
rm -f %{buildroot}/usr/bin/arptables-restore
rm -f %{buildroot}/usr/bin/arptables-save
rm -f %{buildroot}/usr/bin/ebtables
rm -f %{buildroot}/usr/bin/ebtables-nft
rm -f %{buildroot}/usr/bin/ebtables-nft-restore
rm -f %{buildroot}/usr/bin/ebtables-nft-save
rm -f %{buildroot}/usr/bin/ebtables-restore
rm -f %{buildroot}/usr/bin/ebtables-save
rm -f %{buildroot}/usr/bin/ip6tables
rm -f %{buildroot}/usr/bin/ip6tables-legacy
rm -f %{buildroot}/usr/bin/ip6tables-legacy-restore
rm -f %{buildroot}/usr/bin/ip6tables-legacy-save
rm -f %{buildroot}/usr/bin/ip6tables-nft
rm -f %{buildroot}/usr/bin/ip6tables-nft-restore
rm -f %{buildroot}/usr/bin/ip6tables-nft-save
rm -f %{buildroot}/usr/bin/ip6tables-restore
rm -f %{buildroot}/usr/bin/ip6tables-restore-translate
rm -f %{buildroot}/usr/bin/ip6tables-save
rm -f %{buildroot}/usr/bin/ip6tables-translate
rm -f %{buildroot}/usr/bin/iptables
rm -f %{buildroot}/usr/bin/iptables-legacy
rm -f %{buildroot}/usr/bin/iptables-legacy-restore
rm -f %{buildroot}/usr/bin/iptables-legacy-save
rm -f %{buildroot}/usr/bin/iptables-nft
rm -f %{buildroot}/usr/bin/iptables-nft-restore
rm -f %{buildroot}/usr/bin/iptables-nft-save
rm -f %{buildroot}/usr/bin/iptables-restore
rm -f %{buildroot}/usr/bin/iptables-restore-translate
rm -f %{buildroot}/usr/bin/iptables-save
rm -f %{buildroot}/usr/bin/iptables-translate
rm -f %{buildroot}/usr/bin/iptables-xml
rm -f %{buildroot}/usr/bin/nfnl_osf
rm -f %{buildroot}/usr/bin/xtables-legacy-multi
rm -f %{buildroot}/usr/bin/xtables-monitor
rm -f %{buildroot}/usr/bin/xtables-nft-multi
rm -f %{buildroot}/usr/include/libiptc/ipt_kernel_headers.h
rm -f %{buildroot}/usr/include/libiptc/libip6tc.h
rm -f %{buildroot}/usr/include/libiptc/libiptc.h
rm -f %{buildroot}/usr/include/libiptc/libxtc.h
rm -f %{buildroot}/usr/include/libiptc/xtcshared.h
rm -f %{buildroot}/usr/include/xtables-version.h
rm -f %{buildroot}/usr/include/xtables.h
rm -f %{buildroot}/usr/lib64/libip4tc.so
rm -f %{buildroot}/usr/lib64/libip6tc.so
rm -f %{buildroot}/usr/lib64/libiptc.so
rm -f %{buildroot}/usr/lib64/libxtables.so
rm -f %{buildroot}/usr/lib64/pkgconfig/libip4tc.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libip6tc.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/libiptc.pc
rm -f %{buildroot}/usr/lib64/pkgconfig/xtables.pc
rm -f %{buildroot}/usr/lib64/xtables/libarpt_mangle.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_802_3.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_arp.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_arpreply.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_dnat.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_ip.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_ip6.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_log.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_mark.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_mark_m.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_nflog.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_pkttype.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_redirect.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_snat.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_stp.so
rm -f %{buildroot}/usr/lib64/xtables/libebt_vlan.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_DNAT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_DNPT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_HL.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_LOG.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_MASQUERADE.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_NETMAP.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_REDIRECT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_REJECT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_SNAT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_SNPT.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_ah.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_dst.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_eui64.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_frag.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_hbh.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_hl.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_icmp6.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_ipv6header.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_mh.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_rt.so
rm -f %{buildroot}/usr/lib64/xtables/libip6t_srh.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_CLUSTERIP.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_DNAT.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_ECN.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_LOG.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_MASQUERADE.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_NETMAP.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_REDIRECT.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_REJECT.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_SNAT.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_TTL.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_ULOG.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_ah.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_icmp.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_realm.so
rm -f %{buildroot}/usr/lib64/xtables/libipt_ttl.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_AUDIT.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_CHECKSUM.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_CLASSIFY.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_CONNMARK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_CONNSECMARK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_CT.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_DSCP.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_HMARK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_IDLETIMER.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_LED.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_MARK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_NFLOG.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_NFQUEUE.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_NOTRACK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_RATEEST.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_SECMARK.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_SET.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_SYNPROXY.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TCPMSS.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TCPOPTSTRIP.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TEE.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TOS.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TPROXY.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_TRACE.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_addrtype.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_bpf.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_cgroup.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_cluster.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_comment.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_connbytes.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_connlabel.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_connlimit.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_connmark.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_conntrack.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_cpu.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_dccp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_devgroup.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_dscp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_ecn.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_esp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_hashlimit.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_helper.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_ipcomp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_iprange.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_ipvs.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_length.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_limit.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_mac.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_mark.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_multiport.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_nfacct.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_osf.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_owner.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_physdev.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_pkttype.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_policy.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_quota.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_rateest.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_recent.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_rpfilter.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_sctp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_set.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_socket.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_standard.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_state.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_statistic.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_string.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_tcp.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_tcpmss.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_time.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_tos.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_u32.so
rm -f %{buildroot}/usr/lib64/xtables/libxt_udp.so
rm -f %{buildroot}/usr/share/man/man1/iptables-xml.1
rm -f %{buildroot}/usr/share/man/man8/ip6tables-restore.8
rm -f %{buildroot}/usr/share/man/man8/ip6tables-save.8
rm -f %{buildroot}/usr/share/man/man8/ip6tables.8
rm -f %{buildroot}/usr/share/man/man8/iptables-extensions.8
rm -f %{buildroot}/usr/share/man/man8/iptables-restore.8
rm -f %{buildroot}/usr/share/man/man8/iptables-save.8
rm -f %{buildroot}/usr/share/man/man8/iptables.8
rm -f %{buildroot}/usr/share/man/man8/nfnl_osf.8
rm -f %{buildroot}/usr/share/man/man8/xtables-legacy.8
rm -f %{buildroot}/usr/share/man/man8/xtables-monitor.8
rm -f %{buildroot}/usr/share/man/man8/xtables-nft.8
rm -f %{buildroot}/usr/share/man/man8/xtables-translate.8
rm -f %{buildroot}/usr/share/xtables/pf.os

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libip4tc.so.0
/usr/lib64/libip4tc.so.0.1.0
/usr/lib64/libip6tc.so.0
/usr/lib64/libip6tc.so.0.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/compat-iptables-soname0.1.0/COPYING
