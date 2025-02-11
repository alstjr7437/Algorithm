let wonso = [
    "H", "He",
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba", "*", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra", "**", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv",
    "*", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
    "**", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr"
].map { $0.lowercased() }

for _ in 0..<Int(readLine()!)! {
    let word = Array(readLine()!.lowercased())
    let n = word.count

    var dp = Array(repeating: false, count: n + 1)
    dp[0] = true

    for i in 0..<n {
        if !dp[i] { continue }

        let oneChar = String(word[i])
        if wonso.contains(oneChar) {
            dp[i + 1] = true
        }

        if i + 1 < n {
            let twoChar = String(word[i...i + 1])
            if wonso.contains(twoChar) {
                dp[i + 2] = true
            }
        }
    }

    print(dp[n] ? "YES" : "NO")
}