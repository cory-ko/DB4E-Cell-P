#!/usr/bin/env perl
#
# make RegulonDB flatfile decent TSV
#
# author : Kazuki Oshita (cory@g-language.org)
#

use strict;
use warnings;

use URI::Escape;

my @stack = qw//;

open my $fh, '<', $ARGV[0] || die "cannot open file ".$ARGV[0]." : $!";
while (<$fh>) {
    chomp;

    my $entry = $_;

    if (m{^<br>}) {
        $entry = pop(@stack)." ".$entry;
    }

    $entry =~ s{<br>}{}g;
    $entry =~ s{<.+?>}{}g;
    $entry =~ s{&sigma;}{sigma}g;

    $entry = uri_unescape($entry);

    push @stack, $entry;
}
close $fh;

print join("\n", @stack);
