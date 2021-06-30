package BJ1343;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

/**
 * if xCnt % 4 == 0:
 *  ans += 'AAAA' * (xCnt / 4);
 * else if xCnt % 2 == 0:
 *  ans += 'AAAA' * (xCnt / 4) + 'BB';
 * else:
 *  return "-1";
 *
 */
public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String inputString = st.nextToken();

        Solution s = new Solution();
        String ans = s.solution(inputString);

        bw.write(ans);

        bw.flush();
        bw.close();
        br.close();
    }
}

class Solution {
    static boolean canPutPolyoMino[] = new boolean[501];
    static HashMap<Integer, String> matchValue = new HashMap<>();

    public String solution(String inputString) {
        String ans = "";

        int xCnt = 0;
        for (int i = 0; i < inputString.length(); i++) {
            if(inputString.charAt(i) == 'X') {
                // 끝 문자열 처리
                xCnt += 1;
                 if (i == inputString.length() - 1) {
                     ans = addPolyoMino(ans, xCnt);
                     if (ans == null)
                         return "-1";
                 }
            } else {
                ans = addPolyoMino(ans, xCnt);
                if (ans == null)
                    return "-1";
                ans += ".";
                xCnt = 0;
            }
        }

        return ans;
    }

    private String addPolyoMino(String currentAns, int xCnt) {
        if(xCnt % 4 == 0) {
            for (int j = 0; j < xCnt / 4; j++) {
                currentAns += "AAAA";
            }
        } else if (xCnt % 2 == 0) {
            for (int j = 0; j < xCnt / 4; j++) {
                currentAns += "AAAA";
            }
            currentAns += "BB";
        } else {
            return null;
        }

        return currentAns;
    }
}