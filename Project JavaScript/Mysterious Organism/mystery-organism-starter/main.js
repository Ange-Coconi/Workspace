// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

const pAequorFactory = (specimenNum, dna) => {
  return {
    specimenNum,
    dna,
    mutate() {
      let selectBaseMutated = Math.floor(Math.random() * 15);
      let dnaBases = ['A', 'T', 'C', 'G'];
      dnaBases = dnaBases.filter(base => base !== this.dna[selectBaseMutated]);
      this.dna[selectBaseMutated] = dnaBases[Math.floor(Math.random() * 3)];
    }, 
    compareDNA(pAequor) {
      let countBaseCommune = 0;
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i] === pAequor.dna[i]) countBaseCommune++;
      };
      let ratioDNAShared = Math.floor(countBaseCommune / this.dna.length);
      console.log(`specimen #${this.specimenNum} and specimen #${pAequor.specimenNum} have ${ratioDNAShared}% DNA in common.`);
    },
    willLikelySurvive() {
      let countCG = 0;
      this.dna.forEach(base => {
        if (base === 'C' || base === 'G') countCG++;
      })
      return (countCG / this.dna.length) > 0.6; 
    }
  }
}

let samplepAequor = []
let specimenNum = 0;
while (samplepAequor.length < 30) {
  let newpAequor = pAequorFactory(specimenNum, mockUpStrand())
  if (newpAequor.willLikelySurvive()) {
    samplepAequor.push(newpAequor);
    specimenNum++;
  } 
}

console.log(samplepAequor);


