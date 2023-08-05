fn encode(hand: &Vec<usize>) -> usize {
    let mut code: usize = 0;
    for h in hand.iter() {
        code = 5 * code + h;
    }
    code
}

pub struct Solver {
    shanten: Vec<Vec<usize>>
}
impl Solver {
    pub fn new() -> Self {
        let shanten: Vec<Vec<usize>> = serde_json::from_str(include_str!("shanten.json")).unwrap();
        Self { shanten }
    }

    pub fn shanten(&self, h: &[usize], melds: usize) -> i32 {
        let mut dp = vec![vec![vec![usize::MAX; 2]; 5]; 11];
        dp[0][0][0] = 0;
        for i in 0..3 {
            let code = encode(&(0..9).map(|j| h[9 * i + j]).collect::<Vec<usize>>());
            for x in 0..5 - melds {
                for y in 0..2 {
                    if dp[i][x][y] == usize::MAX {
                        continue;
                    }
                    for a in x..5 - melds {
                        for b in y..2 {
                            dp[i + 1][a][b] = std::cmp::min(
                                dp[i + 1][a][b],
                                dp[i][x][y] + self.shanten[code][(b - y) * 5 + (a - x)]
                            );
                        }
                    }
                }
            }
        }

        for i in 0..7 {
            for x in 0..5 - melds {
                for y in 0..2 {
                    if dp[3 + i][x][y] == usize::MAX {
                        continue;
                    }
                    dp[3 + i + 1][x][y] = std::cmp::min(dp[3 + i + 1][x][y], dp[3 + i][x][y]);

                    if y < 1 {
                        dp[3 + i + 1][x][y + 1] = std::cmp::min(
                            dp[3 + i + 1][x][y + 1],
                            dp[3 + i][x][y] + std::cmp::max(0, 2 - h[9 * 3 + i]),
                        );
                    }
                    if x < 4 - melds {
                        dp[3 + i + 1][x + 1][y] = std::cmp::min(
                            dp[3 + i + 1][x + 1][y],
                            dp[3 + i][x][y] + std::cmp::max(0, 3 - h[9 * 3 + i]),
                        );
                    }
                }
            }
        }

        dp[3 + 7][4 - melds][1] as i32 - 1
    }
}
