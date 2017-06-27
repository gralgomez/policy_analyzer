from __future__ import division
from textanalyzer import *
import math

class ReadabilityTool:

    analyzedVars = {}
    text = ""
    lang = ""
    
    tests_given_lang = {}

    def __init__(self, text = ''):
        self.tests_given_lang['all'] = {}
        self.tests_given_lang['all']["ARI"] = self.ARI
        self.tests_given_lang['all']['Flesch Reading Ease'] = self.FleschReadingEase
        self.tests_given_lang['all']["Flesch-Kincaid Grade Level"] = self.FleschKincaidGradeLevel
        self.tests_given_lang['all']["Gunning Fog Index"] = self.GunningFogIndex
        self.tests_given_lang['all']["SMOG Index"] = self.SMOGIndex
        self.tests_given_lang['all']['Coleman Liau Index'] = self.ColemanLiauIndex
        self.tests_given_lang['all']['LIX'] = self.LIX
        self.tests_given_lang['all']['RIX'] = self.RIX
        #mv
        self.tests_given_lang['all']['New Dale Chall'] = self.NewDaleChall
        self.tests_given_lang['all']['New Dale Chall Grade'] = self.NewDaleChall_grade
        self.tests_given_lang['all']['New Dale Chall_enhanced'] = self.NewDaleChall_enhanced
        self.tests_given_lang['all']['New Dale Chall Grade_enhanced'] = self.NewDaleChall_grade_enhanced
        
        self.tests_given_lang['eng'] = {}
        self.tests_given_lang['eng']["ARI"] = self.ARI
        self.tests_given_lang['eng']['Flesch Reading Ease'] = self.FleschReadingEase
        self.tests_given_lang['eng']["Flesch-Kincaid Grade Level"] = self.FleschKincaidGradeLevel
        self.tests_given_lang['eng']["Gunning Fog Index"] = self.GunningFogIndex
        self.tests_given_lang['eng']["SMOG Index"] = self.SMOGIndex
        self.tests_given_lang['eng']['Coleman Liau Index'] = self.ColemanLiauIndex
        self.tests_given_lang['eng']['LIX'] = self.LIX
        self.tests_given_lang['eng']['RIX'] = self.RIX
        #mv
        self.tests_given_lang['eng']['New Dale Chall'] = self.NewDaleChall
        self.tests_given_lang['eng']['New Dale Chall Grade'] = self.NewDaleChall_grade
        self.tests_given_lang['eng']['New Dale Chall_enhanced'] = self.NewDaleChall_enhanced
        self.tests_given_lang['eng']['New Dale Chall Grade_enhanced'] = self.NewDaleChall_grade_enhanced
        
        self.tests_given_lang['no'] = {}
        self.tests_given_lang['no']["ARI"] = self.ARI
        self.tests_given_lang['no']['Coleman Liau Index'] = self.ColemanLiauIndex
        self.tests_given_lang['no']['LIX'] = self.LIX
        self.tests_given_lang['no']['RIX'] = self.RIX
        
        if text != '':
            self.__analyzeText(text)
                
    def __analyzeText(self, text=''):
        if text != '':
            if text != self.text:
                self.text = text
                #lang = NaiveBayes().classifyText(text)
                #nur vorruebergehend, da das bei mir fehler geworfen hat
                lang = "eng"
                self.lang = lang
                t = textanalyzer(lang)
                t.analyzeText(text)
                words = t.getWords(text)
                charCount = t.getCharacterCount(words)
                wordCount = len(words)
                sentenceCount = len(t.getSentences(text))
                syllableCount = t.countSyllables(words)
                complexwordsCount = t.countComplexWords(text)
                averageWordsPerSentence = wordCount/sentenceCount
                newDaleChallMissingWords = t.countNewDaleChallWordsNotInList(text)
                newDaleChallMissingWords_enhanced = t.countNewDaleChallWordsNotInList_enhanced(text)
                
                analyzedVars = {}
                
                analyzedVars['words'] = words
                analyzedVars['charCount'] = float(charCount)
                analyzedVars['wordCount'] = float(wordCount)
                analyzedVars['sentenceCount'] = float(sentenceCount)
                analyzedVars['syllableCount'] = float(syllableCount)
                analyzedVars['complexwordCount'] = float(complexwordsCount)
                analyzedVars['averageWordsPerSentence'] = float(averageWordsPerSentence)
                analyzedVars['newDaleChallMissingWords'] = float(newDaleChallMissingWords)
                analyzedVars['newDaleChallMissingWords_enhanced'] = float(newDaleChallMissingWords_enhanced)
                self.analyzedVars = analyzedVars
        
     
    
    def ARI(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = 4.71 * (analyzedVars['charCount'] / analyzedVars['wordCount']) + 0.5 * (analyzedVars['wordCount'] / analyzedVars['sentenceCount']) - 21.43
        return score
    
    def FleschReadingEase(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars        
        score = 206.835 - (1.015 * (analyzedVars['averageWordsPerSentence'])) - (84.6 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']))
        return score
    
    def FleschKincaidGradeLevel(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = 0.39 * (analyzedVars['averageWordsPerSentence']) + 11.8 * (analyzedVars['syllableCount']/ analyzedVars['wordCount']) - 15.59
        return score
    
    def GunningFogIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars
        score = 0.4 * ((analyzedVars['averageWordsPerSentence']) + (100 * (analyzedVars['complexwordCount']/analyzedVars['wordCount'])))
        return score
    
    def SMOGIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars        
        score = (math.sqrt(analyzedVars['complexwordCount']*(30/analyzedVars['sentenceCount'])) + 3)
        return score
    
    def ColemanLiauIndex(self, text = ''):
        self.__analyzeText(text)
        score = 0.0
        analyzedVars = self.analyzedVars        
        score = (5.89*(analyzedVars['charCount']/analyzedVars['wordCount']))-(30*(analyzedVars['sentenceCount']/analyzedVars['wordCount']))-15.8
        return score
    
    def LIX(self, text = ''):
        self.__analyzeText(text)
        analyzedVars = self.analyzedVars
        score = 0.0
        longwords = 0.0
        for word in analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = analyzedVars['wordCount'] / analyzedVars['sentenceCount'] + float(100 * longwords) / analyzedVars['wordCount']
        return score
    
    def RIX(self, text = ''):
        self.__analyzeText(text)
        analyzedVars = self.analyzedVars
        score = 0.0
        longwords = 0.0
        for word in analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = longwords / analyzedVars['sentenceCount']
        return score
    
    #mv
    def NewDaleChall(self, text = ''):
    #Raw Score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365
        self.__analyzeText(text)
        score = 0.0
        rawscore = 0.0
        analyzedVars =  self.analyzedVars
        
        pdw = analyzedVars['newDaleChallMissingWords'] / analyzedVars['wordCount'] * 100
        rawscore = 0.1579 * pdw + 0.0496 * analyzedVars['averageWordsPerSentence'] 

        if pdw > 5:
            score = rawscore + 3.6365
        else:
            score = rawscore
        return score
    
    def NewDaleChall_enhanced(self, text = ''):
    #Raw Score = 0.1579*(PDW) + 0.0496*(ASL) + 3.6365
        self.__analyzeText(text)
        score = 0.0
        rawscore = 0.0
        analyzedVars =  self.analyzedVars
        
        pdw = analyzedVars['newDaleChallMissingWords_enhanced'] / analyzedVars['wordCount'] * 100
        rawscore = 0.1579 * pdw + 0.0496 * analyzedVars['averageWordsPerSentence'] 

        if pdw > 5:
            score = rawscore + 3.6365
        else:
            score = rawscore
        return score
    
    #mv
    def NewDaleChall_grade(self, text = ''):
        score = self.NewDaleChall(text)
        
        if score < 5:
            grade = 4
        elif score < 5.5:
            grade = 5
        elif score < 6:
            grade = 6
        elif score < 6.5:
            grade = 7
        elif score < 7:
            grade = 8
        elif score < 7.5: 
            grade = 9  
        elif score < 8:
            grade = 10
        elif score < 8.5:
            grade = 11
        elif score < 9: 
            grade = 12
        elif score < 9.33:
            grade = 13
        elif score < 9.66:
            grade = 14
        elif score < 10: 
            grade = 15  
        else:
            grade = 16

        return grade
    
    def NewDaleChall_grade_enhanced(self, text = ''):
        score = self.NewDaleChall_enhanced(text)
        
        if score < 5:
            grade = 4
        elif score < 5.5:
            grade = 5
        elif score < 6:
            grade = 6
        elif score < 6.5:
            grade = 7
        elif score < 7:
            grade = 8
        elif score < 7.5: 
            grade = 9  
        elif score < 8:
            grade = 10
        elif score < 8.5:
            grade = 11
        elif score < 9: 
            grade = 12
        elif score < 9.33:
            grade = 13
        elif score < 9.66:
            grade = 14
        elif score < 10: 
            grade = 15  
        else:
            grade = 16

        return grade
    
    #mv 
    def get_test_scores(self, text):
        site_scores = {}
        
        for testname in self.tests_given_lang[self.lang].keys():
            site_scores[testname] = self.tests_given_lang[self.lang][testname](text)
        
        return  site_scores
    
    def getReportAll(self, text = ''):
        self.__analyzeText(text)
#        ari = 0.0
#        fleschEase = 0.0
#        fleschGrade = 0.0
#        gunningFog = 0.0
#        smog = 0.0
#        coleman = 0.0
#        
#        ari = self.ARI()
#        fleschEase = self.FleschReadingEase()
#        fleschGrade = self.FleschKincaidGradeLevel()
#        gunningFog = self.GunningFogIndex()
#        smog = self.SMOGIndex()
#        coleman = self.ColemanLiauIndex()
#        lix = self.LIX()
#        rix = self.RIX()
#        
#        print '*' * 70
#        print ' ARI: %.1f' % ari
#        print ' Flesch Reading Ease: %.1f' % fleschEase
#        print ' FleschKincaid Grade Level: %.1f' % fleschGrade
#        print ' Gunning Fog: %.1f' % gunningFog
#        print ' SMOG Index: %.1f' % smog
#        print ' Coleman-Liau Index: %.1f' % coleman
#        print ' LIX : %.1f' % lix
#        print ' RIX : %.1f' % rix
#        print '*' * 70
        
        print "=" * 100
        print "Recommended tests for lang: %s" % self.lang 
        print "=" * 100
        for testname in self.tests_given_lang[self.lang].keys():
            print testname + " : %.2f" % self.tests_given_lang[self.lang][testname](text)
        print "=" * 100
        print "Other tests: (Warning! Use with care)"
        print "=" * 100 
        for testname in self.tests_given_lang["all"].keys():
            if not self.tests_given_lang[self.lang].has_key(testname):
                print testname + " : %.2f" % self.tests_given_lang["all"][testname](text) 
            
 
    def demo(self):
        self = ReadabilityTool()
        text = """
                It is for us the living, rather,
                to be dedicated here to the unfinished
                work which they who fought here have
                thus far so nobly advanced. It is
                rather for us to be here dedicated
                to the great task remaining before us,
                that from these honored dead we take 
                increased devotion to that cause for which they
                gave the last full measure of devotion, that we
                here highly resolve that these dead shall not have
                died in vain, that this nation, under God, shall have a
                new birth of freedom, and that government of the people, by
                the people, for the people, shall not perish from this earth.  
               """
       
        self.__analyzeText(text)
        self.getReportAll(text)
    demo = classmethod(demo) 
    
def demo():
    ReadabilityTool.demo()
    
if __name__ == "__main__":
    ReadabilityTool.demo()
 
 
 
 
 
 
 
 
 
    
    
    
    
