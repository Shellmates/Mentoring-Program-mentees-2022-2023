#!/bin/sh

socat -dd TCP-LISTEN:1337,fork,reuseaddr,su=nobody EXEC:"echo 'shellmates{3V3rYth1NG_1S_l00k1Ng_G00D_Y0U_C4N_start}'"