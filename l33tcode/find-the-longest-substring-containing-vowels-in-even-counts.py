from collections import defaultdict, Counter


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dp = defaultdict(lambda: [0])
        counter = Counter()
        vowels = {"a", "e", "i", "o", "u"}

        changed = [0] if s else []

        for pos, c in enumerate(s):
            if c in vowels:
                counter[c] += 1
                if pos > 0:
                    changed.append(pos - 1)
                if pos != 0:
                    changed.append(pos)
                if pos < len(s) - 1:
                    changed.append(pos + 1)
            for vowel in vowels:
                dp[vowel].append(counter[vowel])

        if changed and changed[-1] != len(s) - 1:
            changed.append(len(s) - 1)

        result = 0

        for start in changed:
            for end in reversed(changed):
                if end - start + 1 < result:
                    break
                if all([(dp[v][end + 1] - dp[v][start]) % 2 == 0 for v in vowels]):
                    result = max(result, end - start + 1)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.findTheLongestSubstring("") == 0

    def test_case2(self):
        assert self.sol.findTheLongestSubstring("eleetminicoworoep") == 13

    def test_case3(self):
        assert self.sol.findTheLongestSubstring("leetcodeisgreat") == 5

    def test_case4(self):
        assert self.sol.findTheLongestSubstring("bcbcbc") == 6

    def test_case5(self):
        assert self.sol.findTheLongestSubstring("") == 0

    def test_case6(self):
        assert self.sol.findTheLongestSubstring("id") == 1

    def test_case7(self):
        assert (
            self.sol.findTheLongestSubstring(
                "lffjsdhuyanjfesetkrgdkvpgjtwzbwtgfkvqggundksswifayuwwqjmrmmckkeiitofogmpcyowdrfijnjxzjgluwevtygrudzngiyrrvuhevzsvczkbxyoiuwbvbthbxlcfvfggzutbqttwuqavnpyubrhqhvdknfbqtmjlaokmopplxufnbvwqkisbamepgmrtxofhqbtfnoxsuxagbstmcwqmaezhwmkgdumkbtcgllwbunsjnjuqfxfzqsevwasangzhodanfrjqxoxvfztsmgzzwjkdudrdpbzrmlrbdoibskxoejobejrdzsducnnqcnlrsfwsppwuwtqynjyoohgszrgebixayoovfgjrjecfqcvffnfgynzikyverhnkxyayyxxhfujbdhtvansaqbfvztazroxxnuelmhyvspwruidqxjajuqybjbclldvqoiwbbriklhyizpiyychnmpftnonhoyqucxqmmggtebueollzzvzdihkjavinoiukzwwcwxainwehtltmyahrwxfhvdgdgxuhbnxkexvaoutgbtzbwydbglcmstgvkmjftjjislhhdxmeljltqslbqbcnkqlrhjqjmqrkferdvtevhwjnniqutzvuljoobornasdjtqfucdhlolvjeiyvdxezvpkrhlbbdfpovqcmbsxecjautohtzxhgwersmesweflvblaxvvpocbwwozemuiybbqbfhtxjqdysjfbsdpeyidrzcvkezhhksozlsywvascxisrfaxruyltjrfuaprflszqlwyrnpplndvcdzhzkgbwztswbslhyytznmbvbnyzxsyivslwcdkflmofxfnwpgaqxfgvufvctxxttacgoibzminxhodcgggafnupokfvgncmwllcqvoqvrwagillaghnklvtoowxxdxrybugykcniwvyhbjdjseznlqczjcopfhsaragzgktcsmnqzumvskmojqlgerujrdxplmwfvbcpvbmesxefqcxmrgqmylwsnfnsihyxsltqazzywjjqyiegyobzyidxvcbuucpepotmhvbnfbjobequugguwfgeamuaymtllkekkrwkubkoyyfcaxapvdgmtqntdiqnbzyogbrawxjncklsmbtviegafobtsznwdrbqfwuvuocaraeharbqusvhtwnwdplkfxvghcugfwjccwgexcoyyilhefsyhnclqrfybyrvbiarxspngszdlwkqqsxtyvyifxsjzjpqkqutndbccjtnumlkscwersxoqnhrzixnkujfbdxdodxpywlidkmdfqxroxzqcpksdkdydrhphpkbfbanvkjrtxhlevyxycugybfyywlnvigfgmyqffhoettytyjskfvkrstjhzgfjbeeanblwoengfrlxfxcwilkbqjvextpubzouyntcaaybaayglgobwbhjgryfgsglrgxeswdkfrzuovparpcaoksllnewddovzkfucmaqoavytejzijbppbsezaptnbhdxmvrqasjaahqwumiulxagtxngxoqybezrtiubdmdbptpedwpifbdrocfkoyrfwpxliwyjpfvjqafhdxmcdjzzwdivhfyvldodkqrcosncqtdotpimopmmdmkzuwacfpnacxmvqtkbyaquaoxqfojwncqxtgnkpynumvuaswxqurdfymrzeigpxekxxrudftwuzpajbvrdipxfniljkifqsgttrdtfidgbvveqyusyvuxvoxurdrryhfnntyfbkwzakywfelhvsbwzxnufksguhpjisuqqwsyqphyyfwcshoemfawdxbbrbtpyoxapijixmpdcjumnghqecwwxjgzdlyiehllfxyddxgjhucbktxmgltvwcyookvjkvyqaqcefaahgywvxxnjufdmqqatgcgfkgyzxkzhilmwkbogyvdoemmgkkhpomxaoluupkbomvtwsvppwvjbqohcujufogifrjxmagstpajuxyizricymbsrwbgwpygmkjptqiwzitfmmpzrhhntocwymbawglgdwbpgbvfkbvqiggznqcsfibeawyzbsrgxfkefwmsyaaskquyagcyxpocfiqaznjsrsgfkdxsjwjgsqdaiggyhrgpkmztpxdlcoipxbakpwahrebmdhbjtlddiixehrxtepbnowaakunjpbxoknuafilhcetwkmrrswjyqyklzpetgngdycfauacoqscflqzruffxncodapyulmxeslethmkgzqyurdjogsvoeibfgwprgbmulpqnhgyucaezptwgpimdqcdlfgvnjniyquhmnbbxxglmkyniowmfewnlwvlsylqnblydkbgxtlfrysxjprfnllafftlzwwpuovrgdkuxanhojnicrgodubywaryshhbtpvkggdawyjuiwdelonkzywbqjcohfsssgqjysuspjvidruiffqxtfnwjmmhfnfrrkhgyejwvcucwhdujyaemmubdtbeomjhfphushtiqynzosswjeuvqzebeuresaqirrfwblprztfhkuyufwgvfzspvxhegbqkzhmowiwfdbcbjpbdujztlzlhgigfkivxklbcgfmuogtaommlvlpttauixczvbmnlzwmfjugytcjanboamgrtpziatwxghvueytwkzhuikbmjauoanadfvhamtoeycggynsswllcxzhgdetilwxkninlvhcozhuiuaqtkglsvjlwgvlkrrincmgxoxsggkpoabjeqmcjrsekkmpuvseihhmwslttrxbjoqwluaeppyabmuwnxdgvnxlnomncpfqvgfdxnzlhfmwslwtlervfzzhirhuzczcgsnpybkhcnckfzphlxssgzjfoyxydvadirjzdxjgoxhxanyckoooruhnimtcsmvmddlyllmppgugzezgdxaswfpkijcgywtyrezviwhdsyjqnksrleqoqhukgrxkeremwjbawbnlbqosxvouqjrmmvykipcazekculbbumkgenhjkahgimjpmpytoyiaoooqnxztgtlunffvszorltqagxdlxbuwockudcqlhwckehlhihqmsbaiyxipdpvnidblplrtignxmfsyulcrojpxlgkmylfolirxehxfkvwadegerqbmyeekpodamemcxtecqijesxxkvwdsocqyuagqylwodgaszazvrdjuvanurfrttixfbasggfxwdulbvwvvjdtfgabhfnsheaqopbepiorywlsktvonhxloppagkgdkobywfivrhowneyfszbqskpxvwjriiqqmhqhkjisksmihttcupfzyylrvsfrtcopvlkcrqghvwelkrqqrffuygsggrbsungonkvakfehnrpfqddsdatofcrcewanzigluouypzotpousidkkcosvmimkcjeiuvaefftmdhmfwjltqemdtmlhadgwymcasllmdetyfggohqfoiphmaadfbhkkdnpeubislwgrkpejxjalpaytzhhbrvrjfpjrcgdfsakeqxexbgfhevhruhhwxsjqtnhxsemsvvxsyevfmmqevdsqergvfphpckbpeoeqyrmmdzafgtshitmibbpoucyynengtaaixahewgvpsiufqxgilmtazymycrxnjajdgpdluhvtftaummsbfureuiptxmedlxothitffouogmucgwznfobcbveengtmqdknzvzzysmjwgnbbykimpjckyzsebcbfpknxbodxpigmfnhxlmywdwptmkzuxxuvhbcixbsgngrtxgbcjuyctaqvzayvzeofbubuyhhgraohnhuelbqrlnbzlxahpsmgwpiflujdazsqrmrmtssudexfiulbyzjgmuucobevbeeofefsekshtdlidbfdbtywhbjerawvfobnadfcbzbkptozixprdqzvrzthhjyrnpajyswpogxvmefzfckgpwadkxzaqktvhzegtqlgxkfynowfmllyjigzldltvwfxseifqqishhuoguviviuvpkfljauaqtmynjwleevsdcsstcydfhlbhlnnyriomuzaxrvwlyyowsmclsudlojdnyjzvpnoegzltxgmeqkbfqdcutwgaupzkpnftkxhbyjcabavxohtkktkdejziuyzrctmkpukfsjbjznarrtgeyvdxrsoyikddlnxuonmbtrkadgmhwjpnvlmoonczsjpjpcevcdvuxqmyfylyfcnqahzynsfqcobglkdehuapfpjgsiztsiobjkcpopbloplalgwzeccjnnkivvqvidmhxcpzefrqrlhjcyyfolyzogmbjiakufyjytmjgjwylwpjvixougyggjmbzarudlmlyhvcxbhuqurxlznwkkrjbyiioumtsmybrtzvibqyvhibxmvgkoiyzmjdrq"
            )
            == 4433
        )

    def test_case8(self):
        assert (
            self.sol.findTheLongestSubstring(
                "aeiou" + "".join(["h"] * 100000) + "aeiou"
            )
            == 100010
        )

    def test_case9(self):
        assert self.sol.findTheLongestSubstring("ixzhsdka") == 6
