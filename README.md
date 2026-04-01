# dfa-automata
Implementation of a Deterministic Finite Automaton (DFA) in Python, applying theoretical concepts from formal languages and automata theory.

# Deterministic Finite Automaton (DFA) — Python Implementation

This project comes directly from my **formal languages and automata** course this semester.
The goal was simple: go from the formal definition of a DFA to a concrete implementation, and verify that both describe exactly the same thing.

---

## What is a DFA?

Formally, an automaton is a **quintuplet** A = (Σ, E, I, F, T) where:

- **Σ** — an alphabet (the set of allowed symbols)                                    
- **E** — a finite set of states                                                      
- **I ⊆ E** — the set of initial states                                               
- **F ⊆ E** — the set of final states                                                 
- **T ⊆ E × Σ × E** — the set of transitions                                          

A transition (p, a, q) means: *"from state p, reading symbol a, go to state q."*

**This is extracted from the course of my university
---

A **concrete example** from the course:

```
A1 = (Σ = {a,b},  E = {p,q,r},  I = {p},  F = {r})

T = { (p,a,p), (p,b,p), (p,a,q), (q,b,r), (r,a,r), (r,b,r) }
```

Which gives the following diagram:

```
         a                    a
         ↙                    ↖
  --> ( p ) ---a---> ( q ) ---b---> (( r ))
         ↖                           ↙
          b                         b
```

State `p` = start, nothing significant read yet  
State `q` = just read an `a`, waiting for a `b`  
State `r` = recognized the pattern → final state

---

In Python, this translates directly to:

```python
transitions = {
    'p': {'a': 'q', 'b': 'p'},
    'q': {'a': 'p', 'b': 'r'},
    'r': {'a': 'r', 'b': 'r'}
}
```

The structure `dict[state][symbol] → next_state` is literally the function
**δ : E × Σ → E** from the formal definition.
The code and the theory say the same thing — just in two different languages.

---

## Features

* Deterministic Finite Automaton (DFA) implementation
* Generic and reusable class design
* Multiple example automata
* Direct mapping between theory (δ function) and code
* Simple and readable structure

---

## Project structure

```
dfa.py — main implementation
```

---

## The DFA class

```python
class DFA:
    def __init__(self, etat_initial: int, transitions: dict, etats_finaux: set):
        ...
    def accepte(self, mot: str) -> bool:
        ...
```

Parameters:
* `etat_initial` — integer representing the starting state
* `transitions` — dictionary `{state: {symbol: next_state}}`
* `etats_finaux` — set of accepting states

---

## Example usage

```python
# DFA: words containing at least one 'a'
transitions = {
    0: {'a': 1, 'b': 0},
    1: {'a': 1, 'b': 1}
}

dfa = DFA(etat_initial=0, transitions=transitions, etats_finaux={1})

dfa.accepte("bbb")     # False
dfa.accepte("bbab")    # True
dfa.accepte("")        # False
```

```python
# DFA: words containing the substring "ab"
transitions_2 = {
    0: {'a': 1, 'b': 0},
    1: {'a': 1, 'b': 2},
    2: {'a': 2, 'b': 2}   # once "ab" is seen, always accepted
}

dfa2 = DFA(etat_initial=0, transitions=transitions_2, etats_finaux={2})

dfa2.accepte("ab")      # True
dfa2.accepte("aab")     # True
dfa2.accepte("ba")      # False
```

---

## What I learned

Implementing the automaton forced me to really understand what "deterministic" means:
for each state and each symbol, there is **exactly one possible transition**.

I also realized that the structure `dict[state][symbol] -> next_state` is literally the transition function
δ : Q × Σ → Q from the course — the code and the formal definition map one-to-one.

Refactoring the code into a class made sense naturally, a DFA has state, and so does an object.

---

## Next steps

* [ ] Add alphabet validation at initialization
* [ ] Implement NFA (Non-deterministic Finite Automata)
* [ ] NFA → DFA conversion (subset construction)
* [ ] DFA minimization (Hopcroft's algorithm)

---

## Run the project

No external dependencies required.

```bash
python dfa.py
```

---

*Personal project — first-year Computer Science student, based on formal languages and automata coursework.*
