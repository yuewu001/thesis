#!/usr/bin/perl -w

my $s;
my $x;
my $y;
my $ncword = 0;
my $cword = 0;

while (<>) {
    $s = $_;
    $s =~ s/\s//g;
    $x = () = $s =~ /[\x00-\x7f]+?/g;
    $y = () = $s =~ /[^\x00-\x7f]+?/g;

    $ncword += $x;
    $cword += $y;
}

$cword /= 3;

print "\n字数统计\n";
print "\t非中文(不含空格):\t$ncword\n";
print "\t中文:\t\t\t$cword\n";

$s = $ncword + $cword;
print "\t共计:\t\t\t$s\n";
