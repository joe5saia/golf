#!/usr/bin/perl

use LWP::Simple qw(get);
use JSON        qw(from_json);
use JSON        qw(decode_json);

my $url = "http://gripapi-static-pd.usopen.com/gripapi/player/46402.json";
my $decoded = decode_json(get($url));

while (my ($k,$v)=each $decoded "$k $v\n"};
