# type effectiveness boost/decreases 
types ={"Water": 
        {
            "Weaknesses":["Grass", "Electric"],
            "Strengths": ["Fire", "Rock", "Ground"],
            "Immunities": [],
            "Ineffective":["Water", "Grass", "Dragon"]
        }, 
        "Fire":
        {
            "Weaknesses": ["Water", "Rock", "Ground"],
            "Strengths": ["Grass", "Ice", "Bug", "Steel"],
            "Immunities": [],
            "Ineffective":["Fire", "Water", "Rock", "Dragon"]
        },
        "Grass":
        {
            "Weaknesses": ["Fire","Ice", "Flying", "Bug", "Poison"],
            "Strengths": ["Water", "Rock", "Ground"],
            "Immunities": [],
            "Ineffective":["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"]
        },
        "Flying":
        {
            "Weaknesses": ["Electric", "Ice", "Rock"],
            "Strengths":["Grass", "Bug", "Fighting"],
            "Immunities":["Ground"],
            "Ineffective":["Electric", "Rock", "Steel"]
        },
        "Normal":
        {
            "Weaknesses": ["Fighting"],
            "Strengths": [],
            "Immunities": ["Ghost"],
            "Ineffective":["Steel", "Rock"]
        },
        "Ghost":
        {
            "Weaknesses": ["Dark", "Ghost"],
            "Strengths": ["Psychic", "Ghost"],
            "Immunities":["Normal", "Fighting"],
            "Ineffective":["Dark"]
        },
        "Psychic":
        {
            "Weaknesses": ["Bug", "Ghost", "Dark"],
            "Strengths": ["Fighting", "Poison"],
            "Immunities": [],
            "Ineffective":["Psychic","Steel"]
        },
        "Dark":
        {
            "Weaknesses":["Fighting", "Bug", "Fairy"],
            "Strengths":["Psychic", "Ghost"],
            "Immunities":["Psychic"],
            "Ineffective": {"Fighting","Dark","Fairy"}
        },
        "Fairy":
        {
            "Weaknesses":["Steel", "Poison"],
            "Strengths":["Fighting", "Dragon", "Dark"],
            "Immunities":["Dragon"],
            "Ineffective": ["Fire", "Poison", "Steel"]
        },
        "Steel":
        {
            "Weaknesses":["Fire", "Fighting", "Ground"],
            "Strengths":["Ice","Rock", "Fairy"],
            "Immunities":["Poison"],
            "Ineffective": ["Fire", "Water", "Electric", "Steel"]
        },
        "Bug":
        {
            "Weaknesses":["Fire", "Flying", "Rock"],
            "Strengths":["Grass", "Psychic", "Dark"],
            "Immunities":[],
            "Ineffective": ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"]
        },
        "Ice":
        {
            "Weaknesses":["Fire", "Fighting", "Rock", "Steel"],
            "Strengths":["Grass", "Ground", "Flying", "Dragon"],
            "Immunities":[],
            "Ineffective": ["Ice"]
        },
        "Dragon":
        {
            "Weaknesses":["Ice", "Dragon", "Fairy"],
            "Strengths":["Dragon"],
            "Immunities":[],
            "Ineffective": ["Steel"]
        },
        "Poison":
        {
            "Weaknesses":["Ground", "Psychic"],
            "Strengths":["Grass","Fairy"],
            "Immunities":[],
            "Ineffective": ["Rock", "Poison", "Ground", "Ghost"]
        },
        "Fighting":
        { 
            "Weaknesses":["Flying","Psychic", "Fairy"],
            "Strengths":["Normal", "Ice","Rock", "Dark","Steel"],
            "Immunities":[],
            "Ineffective": ["Poison", "Flying", "Psychic", "Bug","Fairy"]
        },
        "Rock":
        {
            "Weaknesses":["Fighting","Ground","Steel","Water","Grass"],
            "Strengths":["Fire","Ice","Flying", "Bug"],
            "Immunities":[],
            "Ineffective": ["Fighting","Ground","Steel"]
        },
        "Ground":
        {
            "Weaknesses":["Warer","Grass", "Ice"],
            "Strengths":["Fire","Electric","Poison","Rock","Steel"],
            "Immunities":["Electric"],
            "Ineffective": ["Grass","Bug"]
        },
        "Electric":
        {
            "Weaknesses":["Ground"],
            "Strengths":["Water", "Flying"],
            "Immunities":[],
            "Ineffective": ["Dragon","Grass","Electric"]
        }
        }
