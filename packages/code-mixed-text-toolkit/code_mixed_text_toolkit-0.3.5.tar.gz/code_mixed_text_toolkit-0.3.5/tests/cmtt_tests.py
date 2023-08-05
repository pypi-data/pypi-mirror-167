import unittest
import code_mixed_text_toolkit.data as cmtt_data
import code_mixed_text_toolkit.preprocessing as cmtt_pp

class CMTTTestCase(unittest.TestCase):
  def setUp(self):
    self.load = cmtt_data.load
    self.word_tokenize = cmtt_pp.tokenizer.word_tokenize

  def test_data_load_1(self):
    """Test data loading function 1"""
    result = self.load('https://world.openfoodfacts.org/api/v0/product/5060292302201.json')
    self.assertEqual(result['code'], "5060292302201")

  def test_data_load_2(self):
    """Test data loading function 2"""
    result = self.load('https://gist.githubusercontent.com/rnirmal/e01acfdaf54a6f9b24e91ba4cae63518/raw/6b589a5c5a851711e20c5eb28f9d54742d1fe2dc/datasets.csv')
    self.assertEqual(result['about'][20], "Tate Collection metadata")
    self.assertEqual(len(result['about']), 61)

  def test_word_tokenize(self):
    """Test word tokenize function"""
    text = "This Python interpreter is in a conda environment, but the environment has not been activated.  Libraries may fail to load.  To activate this environment"
    result  = cmtt_pp.tokenizer.word_tokenize(text)
    self.assertEqual(len(result), 24)
  
if __name__ == '__main__':
  unittest.main()