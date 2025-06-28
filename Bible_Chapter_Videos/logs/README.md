# 📋 System Logs & Monitoring

**📋 Purpose**: System logs, error tracking, and performance monitoring for Bible Chapter Video Generator  
**🔄 Last Updated**: June 27, 2025  
**📁 Directory Status**: Ready for logging infrastructure

---

## 🎯 **Logging Architecture**

### **📊 Log Categories**

#### **🔄 Processing Logs**
- **`text_processing.log`** - Text processing operations and metrics
- **`api_calls.log`** - JSON2Video and Perplexity API interactions
- **`workflow_execution.log`** - n8n workflow execution details
- **`video_generation.log`** - Video creation process tracking

#### **❌ Error Logs**
- **`errors.log`** - System errors and exceptions
- **`api_errors.log`** - API failures and retry attempts
- **`validation_errors.log`** - Content validation failures
- **`critical.log`** - Critical system failures requiring immediate attention

#### **📈 Performance Logs**
- **`performance.log`** - Processing times and system metrics
- **`costs.log`** - API usage costs and credit tracking
- **`quality_metrics.log`** - Video quality assessment results
- **`success_rates.log`** - Process success/failure statistics

---

## 📝 **Log Format Standards**

### **📋 Standard Log Entry Format**
```
[TIMESTAMP] [LEVEL] [COMPONENT] [MESSAGE] [METADATA]

Example:
[2025-06-27 14:30:15] [INFO] [TextProcessor] Processed Genesis 1:1-31 successfully [wordCount=982, scenes=24, duration=6.5min]
```

### **🏷️ Log Levels**
- **DEBUG**: Detailed diagnostic information
- **INFO**: General operational messages
- **WARNING**: Potential issues that don't stop operation
- **ERROR**: Error conditions that affect functionality
- **CRITICAL**: Serious errors that may stop the system

---

## 🔍 **Monitoring Dashboards**

### **📊 Key Performance Indicators (KPIs)**

#### **🎬 Video Generation Metrics**
- **Daily Video Count**: Number of videos generated per day
- **Success Rate**: Percentage of successful video generations
- **Average Processing Time**: Time from text input to video output
- **Quality Score**: Automated quality assessment ratings

#### **💰 Cost Management**
- **Daily API Costs**: JSON2Video + Perplexity costs
- **Cost Per Video**: Average cost breakdown per video
- **Monthly Budget Tracking**: Progress against monthly limits
- **Credit Usage Alerts**: Low credit warnings

#### **⚡ System Performance**
- **API Response Times**: JSON2Video and Perplexity latency
- **Error Rates**: API failures and retry success
- **Resource Utilization**: System resource consumption
- **Uptime Monitoring**: System availability tracking

---

## 📋 **Log Analysis Tools**

### **🔍 Log Processing Scripts** (Future Development)
```python
# Example log analysis utilities
def analyze_daily_performance():
    """Generate daily performance report from logs."""
    pass

def track_api_costs():
    """Calculate and alert on API cost trends."""
    pass

def quality_trend_analysis():
    """Analyze video quality trends over time."""
    pass
```

### **📊 Automated Reports**
- **Daily Summary**: Performance, costs, issues
- **Weekly Trends**: Quality metrics, success rates
- **Monthly Analytics**: Comprehensive system analysis
- **Alert Notifications**: Real-time issue detection

---

## 🚨 **Alert System**

### **⚠️ Alert Categories**

#### **🔴 Critical Alerts**
- **API Key Expiration**: Before keys expire
- **Credit Depletion**: When API credits run low
- **System Failures**: When core components fail
- **Quality Degradation**: When video quality drops significantly

#### **🟡 Warning Alerts**
- **High Error Rates**: When errors exceed normal thresholds
- **Slow Performance**: When processing times increase
- **Cost Overruns**: When daily costs exceed targets
- **Template Issues**: When template validation fails

#### **🟢 Information Alerts**
- **Daily Summaries**: End-of-day performance reports
- **Milestone Achievements**: When reaching production goals
- **System Updates**: When configurations change
- **Success Celebrations**: When everything runs perfectly

---

## 📈 **Performance Baselines**

### **🎯 Target Metrics**
```yaml
# Performance Standards
video_generation:
  success_rate: ">95%"
  avg_processing_time: "<8 minutes"
  quality_score: ">4.5/5.0"

api_performance:
  response_time: "<5 seconds"
  error_rate: "<2%"
  uptime: ">99.5%"

cost_management:
  cost_per_video: "<$1.50"
  daily_budget: "<$50"
  monthly_budget: "<$1000"
```

### **📊 Historical Baselines**
- **Processing Time**: Track improvements over time
- **Quality Scores**: Monitor consistency and trends
- **Cost Efficiency**: Identify optimization opportunities
- **Error Patterns**: Learn from failure modes

---

## 🔧 **Log Management**

### **📁 Log Rotation Strategy**
```
logs/
├── current/              # Active logs (today)
├── daily/               # Daily archives (last 30 days)
├── weekly/              # Weekly summaries (last 12 weeks)
├── monthly/             # Monthly archives (last 12 months)
└── annual/              # Yearly archives (permanent)
```

### **💾 Storage Management**
- **Retention Policy**: Keep detailed logs for 30 days, summaries for 1 year
- **Compression**: Automatic compression of archived logs
- **Backup**: Regular backup of critical logs
- **Cleanup**: Automated cleanup of old log files

---

## 🛠️ **Troubleshooting Workflows**

### **🔍 Common Issue Debugging**

#### **Video Generation Failures**
1. Check `workflow_execution.log` for n8n errors
2. Review `api_calls.log` for API issues
3. Validate `text_processing.log` for input problems
4. Examine `video_generation.log` for rendering issues

#### **Quality Problems**
1. Review `quality_metrics.log` for patterns
2. Check `validation_errors.log` for content issues
3. Analyze `performance.log` for timing problems
4. Examine template variables in processing logs

#### **Cost Overruns**
1. Check `costs.log` for usage spikes
2. Review `api_calls.log` for unexpected volume
3. Analyze `performance.log` for inefficiencies
4. Monitor credit usage patterns

---

## 📊 **Integration Points**

### **🔄 n8n Workflow Integration**
- **Workflow Logging**: Capture n8n execution details
- **Error Handling**: Route errors to appropriate log files
- **Performance Tracking**: Monitor workflow step timing
- **Success Metrics**: Track workflow completion rates

### **📈 Business Intelligence**
- **Data Export**: Export logs for analysis tools
- **Dashboard Integration**: Feed monitoring dashboards
- **Trend Analysis**: Historical performance analysis
- **Predictive Analytics**: Forecast system needs

---

**💡 Note**: This directory is prepared for comprehensive system monitoring. Current logging is handled within individual workflow components. 