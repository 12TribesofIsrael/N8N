# 🤖 Automation Scripts Guide

**📋 Document Version**: `v2.1.0`  
**🔄 Last Updated**: January 2, 2025  
**🎯 Purpose**: Complete guide to automated text processing and formatting scripts

---

## 🚀 **Scripture Text Processor - `biblical_text_processor.py`**

### **🎯 Purpose**
Automatically formats large bodies of biblical text for optimal video generation input, limiting to 1000 words maximum while preserving sentence structure and biblical accuracy.

### **✨ Key Features**
- ✅ **Auto Word Limiting**: Automatically limits to 1000 words (optimal for 5-7 minute videos)
- ✅ **File-Based Input**: Reads from `Input` file for easy text management
- ✅ **Smart Text Cleaning**: Removes verse references, section headers, and formatting issues
- ✅ **Sentence Preservation**: Truncates at complete sentences for natural flow
- ✅ **Video Metrics**: Calculates expected video length and scene count
- ✅ **Auto-Save Output**: Generates processed text files with word count in filename

---

## 📊 **Script Specifications**

### **Input Requirements**
- **File**: `Input` (plain text file in same directory)
- **Content**: Raw biblical text of any length
- **Format**: Plain text (handles verse numbers, references, formatting)

### **Output Features**
- **Word Limit**: Maximum 1000 words (configurable)
- **Expected Video**: 5-7 minutes at 150 WPM speech rate
- **Scene Estimate**: ~25 scenes (40 words per scene average)
- **Auto-Save**: `processed_biblical_text_{wordcount}words.txt`

### **Performance Metrics**
| Input Size | Processing Time | Output Quality |
|------------|----------------|----------------|
| **Short Text** (200-500 words) | < 1 second | ✅ No truncation needed |
| **Medium Text** (500-1000 words) | < 1 second | ✅ Minimal or no truncation |
| **Large Text** (1000+ words) | < 2 seconds | ✅ Smart truncation at sentences |
| **Very Large** (5000+ words) | < 3 seconds | ✅ Preserves first 1000 words optimally |

---

## 🛠️ **Usage Instructions**

### **Step 1: Prepare Your Text**
```bash
# Create or edit the Input file
notepad Input

# Paste your biblical text (any length)
# Example: Complete Bible chapter, multiple chapters, or passages
```

### **Step 2: Run the Processor**
```bash
# Navigate to Bible_Chapter_Videos folder
cd Bible_Chapter_Videos

# Run the script
python biblical_text_processor.py
```

### **Step 3: Use the Output**
```bash
# The script will display:
# - Processing statistics
# - Expected video metrics
# - Formatted text ready for n8n

# Copy the processed text and paste into your n8n workflow
# Or use the auto-saved file: processed_biblical_text_XXXwords.txt
```

---

## 📋 **Script Output Example**

### **Console Output**
```
============================================================
📖 BIBLICAL TEXT PROCESSOR FOR VIDEO GENERATION
============================================================
🎯 Automatically limits text to 1000 words maximum
📹 Optimized for 20-scene biblical video generation
⏱️  Generates 5-7 minute videos at 150 WPM
------------------------------------------------------------

📂 Reading biblical text from 'Input' file...
✅ Successfully loaded text from Input file
📄 Raw text length: 4,327 characters

🔄 Processing text...
📊 Original word count: 784 words
✅ Processed word count: 784 words
🎬 Expected video length: 5.2 minutes
🎭 Expected scenes: 19 scenes

============================================================
📋 PROCESSED TEXT (Ready for n8n workflow):
============================================================
In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness.
============================================================

💡 Copy the text above and paste it into your n8n workflow
🎯 This will generate approximately 5.2 minutes of video

💾 ✅ Processed text automatically saved to: processed_biblical_text_784words.txt
```

---

## 🧠 **Technical Features**

### **🧹 Text Cleaning Functions**

#### **1. Verse Reference Removal**
```python
# Removes patterns like "Genesis 1:1", "Matthew 5:3-7"
text = re.sub(r'\b[A-Za-z]+\s+\d+:\d+(-\d+)?\s+', '', text)
```

#### **2. Verse Number Cleanup**
```python
# Removes standalone verse numbers like "1", "2", "3"
text = re.sub(r'\s+\d+\s+', ' ', text)
```

#### **3. Section Header Removal**
```python
# Removes study Bible headers and commentary
text = re.sub(r'Precepts to [^:]+:', '', text)
```

#### **4. Whitespace Normalization**
```python
# Converts multiple spaces/newlines to single spaces
text = re.sub(r'\s+', ' ', text)
```

### **📏 Smart Truncation Logic**

#### **Complete Sentence Preservation**
```python
def limit_to_words(words, max_words=1000):
    # Find last complete sentence within word limit
    last_period = text_so_far.rfind('.')
    last_exclamation = text_so_far.rfind('!')
    last_question = text_so_far.rfind('?')
    last_sentence_end = max(last_period, last_exclamation, last_question)
    
    # Truncate at sentence boundary
    if last_sentence_end > 0:
        return clean_text_end.split()
```

### **📊 Video Metrics Calculation**
```python
# Expected video length (150 WPM standard)
expected_minutes = word_count / 150

# Expected scene count (40 words per scene average)
expected_scenes = word_count // 40
```

---

## 🔧 **Customization Options**

### **⚙️ Configurable Parameters**

#### **Word Limit Adjustment**
```python
# In main() function, change max_words parameter
limited_words = limit_to_words(words, max_words=1200)  # Increase to 1200 words
```

#### **Speech Rate Modification**
```python
# Adjust for different voice speeds
expected_minutes = word_count / 120  # Slower speech (120 WPM)
expected_minutes = word_count / 180  # Faster speech (180 WPM)
```

#### **Scene Density Adjustment**
```python
# Adjust words per scene calculation
expected_scenes = word_count // 50   # Longer scenes (50 words)
expected_scenes = word_count // 30   # Shorter scenes (30 words)
```

### **🎛️ Advanced Customization**

#### **Custom Text Cleaning Rules**
```python
def clean_text(text):
    # Add your own cleaning rules
    text = re.sub(r'YOUR_PATTERN_HERE', '', text)
    return text
```

#### **Output Format Modification**
```python
def format_output(words):
    # Customize output formatting
    # Current: 2 sentences per paragraph
    # Modify for different formatting
```

---

## 📁 **Version Control for Scripts**

### **🏷️ Script Versioning**

#### **Current Version**: `biblical_text_processor-v1.1.0.py`
**Features**:
- File-based input system
- Auto-save functionality
- Video metrics calculation
- Smart sentence truncation

#### **Future Versions**:
- **v1.2.0**: Batch processing for multiple files
- **v1.3.0**: Custom cleaning rules configuration
- **v2.0.0**: GUI interface for easier use

### **📦 Including Scripts in Releases**

**When creating new releases, include:**
```
RELEASES/v3.1.0/
├── BHI-Workflow-v3.1.0.json
├── BHI-Template-v3.1.0.json
├── biblical_text_processor-v1.1.0.py    # ← Include script
└── RELEASE_NOTES_v3.1.0.md
```

---

## 🔍 **Troubleshooting**

### **🐛 Common Issues**

#### **Issue**: "Input file not found"
**Solution**: 
```bash
# Create the Input file
notepad Input
# Add your biblical text and save
```

#### **Issue**: "No words found after cleaning"
**Solution**: Check if input file contains actual text, not just formatting characters

#### **Issue**: "Text too short for video"
**Solution**: Add more biblical content to Input file for longer videos

#### **Issue**: "Python not found"
**Solution**: 
```bash
# Install Python 3.7+
# Or use full path
C:\Python39\python.exe biblical_text_processor.py
```

### **💡 Best Practices**

1. **Input Quality**: Use clean biblical text without excessive formatting
2. **File Management**: Keep Input file updated with current content
3. **Output Review**: Always review processed text before using in workflows
4. **Backup**: Save important processed files to prevent re-work

---

## 🚀 **Integration with Video Workflows**

### **🔗 Workflow Integration**

#### **Standard Process**:
1. **Prepare Text**: Add biblical content to `Input` file
2. **Process**: Run `python biblical_text_processor.py`
3. **Copy Output**: Use processed text in n8n workflow
4. **Generate Video**: Execute n8n workflow for video creation

#### **Advanced Integration**:
```python
# Future enhancement: Direct n8n API integration
# Script could automatically submit processed text to workflow
```

### **📊 Quality Assurance**

#### **Pre-Processing Checklist**:
- [ ] Input file contains biblical text
- [ ] Text is relevant and appropriate
- [ ] No copyrighted material included
- [ ] Content aligns with video purpose

#### **Post-Processing Validation**:
- [ ] Word count within acceptable range (600-1000 optimal)
- [ ] Sentences complete and natural
- [ ] Biblical accuracy preserved
- [ ] No formatting artifacts remain

---

**🏆 SUMMARY**: The `biblical_text_processor.py` script is a powerful automation tool that streamlines the video creation process by optimally formatting biblical text for video generation workflows. It saves time, ensures consistency, and maintains biblical accuracy while optimizing for video length and quality.** 