package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

type File struct {
	size int
}

type Directory struct {
	files   map[string]File
	dirs    map[string]Directory
	size    int
	cumSize int
}

func construct_fs(lines *[]string, pos int, dir *Directory) int {
	for pos >= len(*lines) {
	}

	if (*lines)[pos] != "$ ls" {
		panic("hm")
	}

	fmt.Println((*lines)[pos])

	for pos < len(*lines) && (*lines)[pos] != "$ cd .." {
		fmt.Println((*lines)[pos])
		if (*lines)[pos] == "$ ls" {
			fmt.Println((*lines)[pos])

			pos += 1

			fmt.Println((*lines)[pos])

			fmt.Println(dir)

			for pos < len(*lines) && (*lines)[pos][0] != '$' {
				fmt.Println((*lines)[pos])
				tmp := strings.Split((*lines)[pos], " ")
				if tmp[0] == "dir" {
					dir.dirs[tmp[1]] = Directory{map[string]File{}, map[string]Directory{}, 0, 0}
				} else {
					size, _ := strconv.Atoi(tmp[0])
					fmt.Println(size)
					dir.files[tmp[1]] = File{size}
					dir.size += size
					fmt.Println(dir.size)
				}
				pos += 1
			}

			fmt.Println(dir)
		} else if (*lines)[pos][:4] == "$ cd" {
			name := (*lines)[pos][5:]

			nextDir := dir.dirs[name]
			fmt.Println((*lines)[pos], name, &nextDir)

			pos = construct_fs(lines, pos+1, &nextDir)

			dir.dirs[name] = nextDir
		}
	}

	return pos + 1
}

func dirSizeBelow(dir *Directory, threshold int) (int, int) {
	fmt.Println(dir)
	cumSum := dir.size

	answer := 0

	for _, nextDir := range dir.dirs {
		nextCumSum, nextAnswer := dirSizeBelow(&nextDir, threshold)

		cumSum += nextCumSum
		answer += nextAnswer
	}

	if cumSum <= threshold {
		answer += cumSum
	}

	dir.cumSize = cumSum

	return cumSum, answer
}

func smallestDirMoreThan(dir *Directory, limit int) (int, int) {
	answer := math.MaxInt64

	fmt.Println(123, answer)

	tmp := dir.size

	for _, nextDir := range dir.dirs {
		cumSum, answer2 := smallestDirMoreThan(&nextDir, limit)
		tmp += cumSum

		if answer2 < answer {
			answer = answer2
		}
	}

	fmt.Println(234, tmp, answer)
	if tmp > limit && answer > tmp {
		answer = tmp
	}

	return tmp, answer
}

func day07_1(input string) int {
	lines := strings.Split(input, "\n")
	rootDir := Directory{map[string]File{}, map[string]Directory{}, 0, 0}

	construct_fs(&lines, 1, &rootDir)

	_, answer := dirSizeBelow(&rootDir, 100000)

	return answer
}

func day07_2(input string) int {
	lines := strings.Split(input, "\n")
	rootDir := Directory{map[string]File{}, map[string]Directory{}, 0, 0}

	construct_fs(&lines, 1, &rootDir)

	cumSum, _ := dirSizeBelow(&rootDir, 100000)

	rootDir.cumSize = cumSum

	needed := 30000000 - (70000000 - rootDir.cumSize)

	_, a := smallestDirMoreThan(&rootDir, needed)

	return a
}

func day07() {
	input1 := `$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k`
	input2 := `$ cd /
$ ls
dir grdd
270251 hjlvwtph.jzv
230026 jzmgcj.gmd
dir nns
dir rrfflbql
$ cd grdd
$ ls
233044 mqbz.fcp
dir nnch
82939 rgtvsqsh.psq
150253 srvg.dth
$ cd nnch
$ ls
4014 mqbz.fcp
$ cd ..
$ cd ..
$ cd nns
$ ls
dir cgbdghtd
dir dnh
dir gjhp
dir jwjm
dir mrpfzd
dir ncvv
dir pfnglqgw
dir tlh
dir vnrhpc
$ cd cgbdghtd
$ ls
276941 jrrcdgz.szm
$ cd ..
$ cd dnh
$ ls
269539 nnch
220637 sjzmpwwb
$ cd ..
$ cd gjhp
$ ls
dir czclvmwc
dir jgtzfsm
$ cd czclvmwc
$ ls
179729 fzqvvlg
67916 pmsdthr.prv
$ cd ..
$ cd jgtzfsm
$ ls
151591 rcggj.nwm
$ cd ..
$ cd ..
$ cd jwjm
$ ls
203559 nnch
$ cd ..
$ cd mrpfzd
$ ls
dir pfnglqgw
204978 qscs.vpq
16184 tbfwpmp.hvl
$ cd pfnglqgw
$ ls
dir wvzw
dir ztl
$ cd wvzw
$ ls
195912 jpn.ndh
143238 nnch.djz
2239 pmsdthr.prv
dir sfqq
$ cd sfqq
$ ls
134913 pthmqd
dir vcdhz
$ cd vcdhz
$ ls
13800 ffhv.jnq
$ cd ..
$ cd ..
$ cd ..
$ cd ztl
$ ls
181007 mqbz.fcp
266517 zbpjz.gbr
$ cd ..
$ cd ..
$ cd ..
$ cd ncvv
$ ls
296494 ccmvjm.bjb
20801 hjr
32494 mqbz.fcp
dir nnch
dir pfnglqgw
dir qpq
dir rftzzmq
dir wgblcl
294511 wrdmgdb.fmh
$ cd nnch
$ ls
dir hjzpfvm
dir ncvv
dir pffr
dir pfnglqgw
dir ssdffgsq
$ cd hjzpfvm
$ ls
304078 mqbz.fcp
dir nnch
146425 nnch.lrw
dir vcfglm
dir zhscvh
$ cd nnch
$ ls
311625 gqmpvplj.vjg
248744 ndfcj
$ cd ..
$ cd vcfglm
$ ls
dir btptvs
dir ghpvzvzp
146354 nnch
$ cd btptvs
$ ls
127157 nqnnwq.rtz
16115 pmsdthr.prv
$ cd ..
$ cd ghpvzvzp
$ ls
dir ncvv
$ cd ncvv
$ ls
236869 pmsdthr.prv
$ cd ..
$ cd ..
$ cd ..
$ cd zhscvh
$ ls
225337 glpz
$ cd ..
$ cd ..
$ cd ncvv
$ ls
dir nljtcssr
dir svjhsvjh
$ cd nljtcssr
$ ls
258085 gqmpvplj.vjg
dir ncvv
dir qmzfgcr
249049 wznr.gbs
dir zvvpqlmq
$ cd ncvv
$ ls
147686 ndfcj.sfr
$ cd ..
$ cd qmzfgcr
$ ls
162245 ndfcj.nlj
$ cd ..
$ cd zvvpqlmq
$ ls
160481 ggnc
$ cd ..
$ cd ..
$ cd svjhsvjh
$ ls
dir bjqbmt
58138 gqmpvplj.vjg
dir nsvf
154398 rrhjs.gch
dir wmvhmlr
$ cd bjqbmt
$ ls
252614 ndfcj.wzg
153886 nnch
214625 zhmdvb
$ cd ..
$ cd nsvf
$ ls
274932 nnch.jfg
$ cd ..
$ cd wmvhmlr
$ ls
137205 nnch
$ cd ..
$ cd ..
$ cd ..
$ cd pffr
$ ls
89895 cwpnzngf.swg
197833 jgv
184768 jjhzddp.fbb
31033 tpngfdsg.brv
$ cd ..
$ cd pfnglqgw
$ ls
228015 ccmvjm.bjb
$ cd ..
$ cd ssdffgsq
$ ls
165887 gqmpvplj.vjg
dir lfq
dir nnch
170828 qjb.mnp
dir ttj
$ cd lfq
$ ls
257411 gqmpvplj.vjg
137375 jzmgcj.gmd
267329 nsbsgd.zvq
$ cd ..
$ cd nnch
$ ls
dir mrfwfq
171186 ndhqthf.jlp
$ cd mrfwfq
$ ls
100447 lsfsh.mvr
$ cd ..
$ cd ..
$ cd ttj
$ ls
49634 ndfcj
dir tqvld
$ cd tqvld
$ ls
dir ndfcj
$ cd ndfcj
$ ls
dir gnzj
80690 pmlnbvj
12843 zbrfmfgj.lzr
$ cd gnzj
$ ls
dir wtpzrpn
$ cd wtpzrpn
$ ls
33840 gqmpvplj.vjg
18122 rrfflbql.vws
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
289092 fdjfvb
$ cd ..
$ cd qpq
$ ls
126281 ccmvjm.bjb
dir crtzrd
231988 jzmgcj.gmd
203061 mgmmp
272098 mqbz.fcp
dir pfnglqgw
dir qzvcsn
105003 rrfflbql.mcm
$ cd crtzrd
$ ls
162336 fsps
100215 mctd.wsz
67983 mqbz.fcp
281538 mqq.cgz
dir ndfcj
dir rrfflbql
dir wbmtvr
$ cd ndfcj
$ ls
290647 pfjczr.wjc
$ cd ..
$ cd rrfflbql
$ ls
dir mpr
dir ncvv
dir rrfflbql
301818 zml.qfj
$ cd mpr
$ ls
237300 gqmpvplj.vjg
dir pfnglqgw
$ cd pfnglqgw
$ ls
dir brnwdjtg
dir dvqlmzw
248787 pmsdthr.prv
$ cd brnwdjtg
$ ls
256129 ncvv
dir ptztp
$ cd ptztp
$ ls
104775 nnch.wlc
$ cd ..
$ cd ..
$ cd dvqlmzw
$ ls
25407 twgqbrtl
$ cd ..
$ cd ..
$ cd ..
$ cd ncvv
$ ls
dir jvwvsm
62293 jzmgcj.gmd
261836 mqbz.fcp
dir vvvrf
$ cd jvwvsm
$ ls
222978 ccmvjm.bjb
207799 jzmgcj.gmd
dir pcvsvcn
248569 pmsdthr.prv
dir wmd
$ cd pcvsvcn
$ ls
39803 pmsdthr.prv
$ cd ..
$ cd wmd
$ ls
9516 rfstbvj.nhz
$ cd ..
$ cd ..
$ cd vvvrf
$ ls
dir ncvv
dir znwc
$ cd ncvv
$ ls
110667 jzmgcj.gmd
$ cd ..
$ cd znwc
$ ls
182248 ndfcj.crv
$ cd ..
$ cd ..
$ cd ..
$ cd rrfflbql
$ ls
231013 ccmvjm.bjb
dir jlc
dir rrfflbql
79210 ttm.zmw
$ cd jlc
$ ls
28096 ccmvjm.bjb
113156 pmsdthr.prv
$ cd ..
$ cd rrfflbql
$ ls
234558 lbg.bpn
$ cd ..
$ cd ..
$ cd ..
$ cd wbmtvr
$ ls
285832 fqhs
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
110965 nnch
195414 pmsdthr.prv
243812 thcpw.jfw
$ cd ..
$ cd qzvcsn
$ ls
279179 gqmpvplj.vjg
191705 mhmlfc.czv
146298 pfnglqgw.ppm
2775 pmsdthr.prv
$ cd ..
$ cd ..
$ cd rftzzmq
$ ls
310418 bddhlvs.rwm
152681 cdznrjl
278447 rrfflbql
dir tmcltf
$ cd tmcltf
$ ls
dir mzr
$ cd mzr
$ ls
24154 ccmvjm.bjb
dir nnch
dir rqsbw
$ cd nnch
$ ls
100523 mqbz.fcp
$ cd ..
$ cd rqsbw
$ ls
64033 czzqg.pcz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wgblcl
$ ls
235768 dvdzbgv.vwl
186757 jzmgcj.gmd
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
129407 zfphqcsf.cfn
$ cd ..
$ cd tlh
$ ls
89310 jzmgcj.gmd
21486 nwnbbmr.lsq
40023 rdmtp.zsf
$ cd ..
$ cd vnrhpc
$ ls
104731 gqmpvplj.vjg
176015 grn
3646 jzmgcj.gmd
dir ncvv
45414 nfrj.lvq
233767 pfnglqgw.bvf
$ cd ncvv
$ ls
252691 ccmvjm.bjb
dir ncvv
dir vwv
dir wwmwfbf
$ cd ncvv
$ ls
306441 qfhhnmqz.snc
$ cd ..
$ cd vwv
$ ls
56033 rrfflbql
$ cd ..
$ cd wwmwfbf
$ ls
45964 gqmpvplj.vjg
118391 mvwl
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rrfflbql
$ ls
175540 bcw.sqp
154750 ggncvs.nvn
dir jqzm
dir mgbglnr
192820 ndfcj
dir pfnglqgw
217147 qjng.svz
dir rrfflbql
$ cd jqzm
$ ls
dir ncvv
dir nfcvcddz
242934 rjwlgm
dir wzj
$ cd ncvv
$ ls
298067 pfnglqgw.jdv
$ cd ..
$ cd nfcvcddz
$ ls
261264 gqmpvplj.vjg
19464 mqbz.fcp
121507 ncqhrf
dir ndfcj
58485 ndfcj.vhh
dir rcrzjm
228359 wnftnshq
$ cd ndfcj
$ ls
309008 bwn
$ cd ..
$ cd rcrzjm
$ ls
48178 fgzpwhvt
129342 qns.lnj
$ cd ..
$ cd ..
$ cd wzj
$ ls
91384 gqmpvplj.vjg
dir nnch
dir rzm
$ cd nnch
$ ls
dir sgbwrl
$ cd sgbwrl
$ ls
dir ndfcj
$ cd ndfcj
$ ls
295624 cbmdr
$ cd ..
$ cd ..
$ cd ..
$ cd rzm
$ ls
dir cprj
86746 dfwsj.hqq
dir dljnvq
dir ndfcj
159465 nsglq
202670 pfnglqgw.wbh
29700 rrfflbql.wln
dir vgtftq
$ cd cprj
$ ls
148192 gqmpvplj.vjg
165473 hwp.ltc
$ cd ..
$ cd dljnvq
$ ls
91675 pmsdthr.prv
$ cd ..
$ cd ndfcj
$ ls
83124 rrfflbql.ghs
$ cd ..
$ cd vgtftq
$ ls
186744 mqbz.fcp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd mgbglnr
$ ls
dir ddtcz
dir ncvv
dir nhpwf
dir rrfflbql
203683 ttbc
dir tvbjgv
dir wvzcq
$ cd ddtcz
$ ls
61553 wfzj
$ cd ..
$ cd ncvv
$ ls
37589 ccmvjm.bjb
87987 dnct
196537 ndfcj.cqg
40448 pmsdthr.prv
$ cd ..
$ cd nhpwf
$ ls
243345 gqmpvplj.vjg
53165 nnch.gfc
dir pfnglqgw
dir vdnnf
$ cd pfnglqgw
$ ls
131411 mhvzv.scz
142119 nnch.gnt
$ cd ..
$ cd vdnnf
$ ls
83904 ccmvjm.bjb
dir czfqdtd
dir dgblftbz
dir jnftbbtm
dir pfbnl
dir pfnglqgw
$ cd czfqdtd
$ ls
dir nnch
$ cd nnch
$ ls
255744 ndfcj.ldv
$ cd ..
$ cd ..
$ cd dgblftbz
$ ls
278883 ncvv.zph
dir pfnglqgw
133315 phns.cmq
130316 sftj
$ cd pfnglqgw
$ ls
174155 vnwtv
$ cd ..
$ cd ..
$ cd jnftbbtm
$ ls
255828 nmln
30605 pfnglqgw
$ cd ..
$ cd pfbnl
$ ls
8603 ndfcj
$ cd ..
$ cd pfnglqgw
$ ls
235364 pmsdthr.prv
$ cd ..
$ cd ..
$ cd ..
$ cd rrfflbql
$ ls
dir gfgbj
$ cd gfgbj
$ ls
215226 jzmgcj.gmd
$ cd ..
$ cd ..
$ cd tvbjgv
$ ls
dir nnch
$ cd nnch
$ ls
dir gmsb
$ cd gmsb
$ ls
dir tlqdvpr
$ cd tlqdvpr
$ ls
130013 hzrq.zrg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd wvzcq
$ ls
dir ncvv
$ cd ncvv
$ ls
103168 ccmvjm.bjb
18537 ncvv
dir nnch
dir rrfflbql
$ cd nnch
$ ls
20928 ndfcj.lln
$ cd ..
$ cd rrfflbql
$ ls
dir lgfwf
$ cd lgfwf
$ ls
dir fmzqt
dir rrfflbql
$ cd fmzqt
$ ls
301419 gqmpvplj.vjg
$ cd ..
$ cd rrfflbql
$ ls
dir nbvqch
$ cd nbvqch
$ ls
298966 csqvdql.cwr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
dir bhmndjpq
203077 fssbcjcm.hvt
dir lfslp
dir ncvv
dir nftdcrl
dir nnch
dir pfnglqgw
dir qfbbnr
dir wttc
$ cd bhmndjpq
$ ls
299744 cmgwwccb.tvv
173562 fpwv
dir hmnbfdtr
dir jqpcs
73425 mqbz.fcp
dir ncvv
dir ndfcj
95707 pmsdthr.prv
dir ptzdv
dir qzhrsnqh
dir sbqg
$ cd hmnbfdtr
$ ls
dir pfnglqgw
dir qmpplbtv
77228 tvpdstcn.zbb
$ cd pfnglqgw
$ ls
dir dwr
dir jmgp
102634 mqbz.fcp
148654 ncvv
257637 ncvv.nzn
286938 rrfflbql
$ cd dwr
$ ls
141669 ndfcj
9012 ptrlq.stq
$ cd ..
$ cd jmgp
$ ls
78473 pfnglqgw
$ cd ..
$ cd ..
$ cd qmpplbtv
$ ls
202948 wjp.rgt
$ cd ..
$ cd ..
$ cd jqpcs
$ ls
290654 fmmcph
8123 zrr.vqm
$ cd ..
$ cd ncvv
$ ls
dir hbrttp
$ cd hbrttp
$ ls
128004 nffzj
$ cd ..
$ cd ..
$ cd ndfcj
$ ls
dir vscwfsl
$ cd vscwfsl
$ ls
251706 snww.dzb
$ cd ..
$ cd ..
$ cd ptzdv
$ ls
113702 nnch
$ cd ..
$ cd qzhrsnqh
$ ls
118758 gqmpvplj.vjg
75504 vcnn.stz
102737 zvv
$ cd ..
$ cd sbqg
$ ls
287663 bhcpslm.wwt
dir bqr
dir czhfphh
39170 fqn
dir gqnts
267314 hlv.ljc
8701 jqpdpg.prz
dir ncvv
211749 psln.pdq
$ cd bqr
$ ls
dir chjfw
dir dgccfvtl
219440 fvfsfz
262276 jzmgcj.gmd
dir ndfcj
294287 pfnglqgw.lwh
163881 rrfflbql
278231 vgjm.rrh
$ cd chjfw
$ ls
134800 hvmvqbz.bqj
$ cd ..
$ cd dgccfvtl
$ ls
155579 lwmqrd.wvp
$ cd ..
$ cd ndfcj
$ ls
144255 ncvv.hrn
236730 ndfcj
dir pfz
$ cd pfz
$ ls
297448 rrfflbql.fdt
$ cd ..
$ cd ..
$ cd ..
$ cd czhfphh
$ ls
dir wmws
$ cd wmws
$ ls
14499 ncvv
$ cd ..
$ cd ..
$ cd gqnts
$ ls
165940 ccmvjm.bjb
dir gjcm
dir hldzdlrl
dir jtnpgg
dir nnch
287896 pmsdthr.prv
$ cd gjcm
$ ls
125716 gqmpvplj.vjg
dir mhjm
197155 msspbg
176407 trtdggnf
$ cd mhjm
$ ls
18749 jzmgcj.gmd
252999 nnch
76392 rrfflbql.mzh
$ cd ..
$ cd ..
$ cd hldzdlrl
$ ls
dir gzpcgj
dir rvvgn
$ cd gzpcgj
$ ls
dir vfz
$ cd vfz
$ ls
183852 pmsdthr.prv
$ cd ..
$ cd ..
$ cd rvvgn
$ ls
143443 ndfcj
$ cd ..
$ cd ..
$ cd jtnpgg
$ ls
dir dhvd
dir hlmgslbs
dir rrfflbql
dir vmqpcm
$ cd dhvd
$ ls
131598 ltr.rph
$ cd ..
$ cd hlmgslbs
$ ls
173562 rrfflbql
$ cd ..
$ cd rrfflbql
$ ls
dir ghvmc
$ cd ghvmc
$ ls
311611 jzmgcj.gmd
$ cd ..
$ cd ..
$ cd vmqpcm
$ ls
192032 mqbz.fcp
$ cd ..
$ cd ..
$ cd nnch
$ ls
112995 ccmvjm.bjb
$ cd ..
$ cd ..
$ cd ncvv
$ ls
106711 dswpw.wgr
46614 jzmgcj.gmd
115391 mqbz.fcp
dir nnch
61970 pmsdthr.prv
dir rrfflbql
$ cd nnch
$ ls
50060 gqjtv.gcs
dir lnmmd
73078 ncvv
49129 tfb
dir vgwpcjrl
dir wnqlrqlf
$ cd lnmmd
$ ls
71780 gqmpvplj.vjg
$ cd ..
$ cd vgwpcjrl
$ ls
8269 zcspgw
$ cd ..
$ cd wnqlrqlf
$ ls
dir wzsvhssb
$ cd wzsvhssb
$ ls
187249 jzmgcj.gmd
$ cd ..
$ cd ..
$ cd ..
$ cd rrfflbql
$ ls
dir bpzmvds
24889 hfnbzcn
dir lqffwfr
274793 nnch.svh
dir rhwm
$ cd bpzmvds
$ ls
298048 tfnqwpj
$ cd ..
$ cd lqffwfr
$ ls
dir mzfpbjtl
$ cd mzfpbjtl
$ ls
217469 jzmgcj.gmd
$ cd ..
$ cd ..
$ cd rhwm
$ ls
54198 gqmpvplj.vjg
dir tlnmwhdt
$ cd tlnmwhdt
$ ls
94380 ndfcj.bvv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lfslp
$ ls
dir cmrwvp
dir cnh
311549 jgmf.fbs
dir jtgrbqvj
166298 pbwsqpcg.whf
151437 pfnglqgw.mcj
dir sqlwn
$ cd cmrwvp
$ ls
217666 pmsdthr.prv
172469 vzw.rqw
$ cd ..
$ cd cnh
$ ls
84011 jfb.mpt
$ cd ..
$ cd jtgrbqvj
$ ls
dir dcfpfq
dir ghhs
dir ntbmh
dir pfnglqgw
$ cd dcfpfq
$ ls
159731 pfnglqgw
$ cd ..
$ cd ghhs
$ ls
104713 blwnhcn
$ cd ..
$ cd ntbmh
$ ls
174007 jzmgcj.gmd
dir pfnglqgw
60549 rrfflbql.scj
dir zwcdggd
$ cd pfnglqgw
$ ls
49844 rfdw.pqh
$ cd ..
$ cd zwcdggd
$ ls
135925 ccmvjm.bjb
1135 gqmpvplj.vjg
120968 hmgpcj.nbb
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
184937 ccmvjm.bjb
128621 llsjsmg.vtv
dir lsbf
42834 ndfcj.fwq
85391 trrchml.sgp
$ cd lsbf
$ ls
192593 cfdtsfq.sln
289191 nnch.qzj
$ cd ..
$ cd ..
$ cd ..
$ cd sqlwn
$ ls
77962 ccmvjm.bjb
114288 ndfcj
$ cd ..
$ cd ..
$ cd ncvv
$ ls
dir gsd
$ cd gsd
$ ls
14949 jwcp.lmq
$ cd ..
$ cd ..
$ cd nftdcrl
$ ls
185409 jzmgcj.gmd
$ cd ..
$ cd nnch
$ ls
280827 djftt
dir ljt
dir ncvv
dir ndfcj
33396 qvhndl.pwn
136204 qvlc.cbr
14063 rrfflbql.mrq
130666 vscjncbm.sls
$ cd ljt
$ ls
166514 cgrgbpvw
55138 jzmgcj.gmd
$ cd ..
$ cd ncvv
$ ls
dir fhnw
56003 gqtcgszl.vnf
145831 jzmgcj.gmd
dir mwcbd
dir rclnhb
$ cd fhnw
$ ls
28050 gqmpvplj.vjg
$ cd ..
$ cd mwcbd
$ ls
288468 ncvv
$ cd ..
$ cd rclnhb
$ ls
190004 ndjmjbp
$ cd ..
$ cd ..
$ cd ndfcj
$ ls
287125 gqmpvplj.vjg
dir ndfcj
247237 nnch
138902 pfnglqgw
$ cd ndfcj
$ ls
143400 ssvsvffz
$ cd ..
$ cd ..
$ cd ..
$ cd pfnglqgw
$ ls
dir cwwb
dir dtf
97867 mqbz.fcp
$ cd cwwb
$ ls
dir wtz
$ cd wtz
$ ls
300949 zcq
$ cd ..
$ cd ..
$ cd dtf
$ ls
28018 gqmpvplj.vjg
$ cd ..
$ cd ..
$ cd qfbbnr
$ ls
dir bqmdfjp
89207 gjfzv
176709 pmsdthr.prv
246390 rrfflbql.vdl
$ cd bqmdfjp
$ ls
137504 cwz.jdg
9191 ncvv
$ cd ..
$ cd ..
$ cd wttc
$ ls
279516 ccmvjm.bjb
115478 lwnpwdqt.jpj
$ cd ..
$ cd ..
$ cd rrfflbql
$ ls
162371 nnch.pnm`

	fmt.Println(day07_1(input1))
	fmt.Println(day07_1(input2))

	fmt.Println(day07_2(input1))
	fmt.Println(day07_2(input2))
}
