//
// Generated file, do not edit! Created by nedtool 5.4 from routerMsg.msg.
//

#if defined(__clang__)
#  pragma clang diagnostic ignored "-Wreserved-id-macro"
#endif
#ifndef __ROUTERMSG_M_H
#define __ROUTERMSG_M_H

#include <omnetpp.h>

// nedtool version check
#define MSGC_VERSION 0x0504
#if (MSGC_VERSION!=OMNETPP_VERSION)
#    error Version mismatch! Probably this file was generated by an earlier version of nedtool: 'make clean' should help.
#endif



// cplusplus {{
#include <vector>
typedef std::vector<int> IntVector;
// }}

/**
 * Class generated from <tt>routerMsg.msg:24</tt> by nedtool.
 * <pre>
 * packet routerMsg
 * {
 *     IntVector route;
 *     int hopCount = 0;
 *     int messageType;  //0 for transaction, 1 for ack, 2 for balance update
 *     double amount;
 *     int priorityClass;
 *     int transactionId;
 * }
 * </pre>
 */
class routerMsg : public ::omnetpp::cPacket
{
  protected:
    IntVector route;
    int hopCount;
    int messageType;
    double amount;
    int priorityClass;
    int transactionId;

  private:
    void copy(const routerMsg& other);

  protected:
    // protected and unimplemented operator==(), to prevent accidental usage
    bool operator==(const routerMsg&);

  public:
    routerMsg(const char *name=nullptr, short kind=0);
    routerMsg(const routerMsg& other);
    virtual ~routerMsg();
    routerMsg& operator=(const routerMsg& other);
    virtual routerMsg *dup() const override {return new routerMsg(*this);}
    virtual void parsimPack(omnetpp::cCommBuffer *b) const override;
    virtual void parsimUnpack(omnetpp::cCommBuffer *b) override;

    // field getter/setter methods
    virtual IntVector& getRoute();
    virtual const IntVector& getRoute() const {return const_cast<routerMsg*>(this)->getRoute();}
    virtual void setRoute(const IntVector& route);
    virtual int getHopCount() const;
    virtual void setHopCount(int hopCount);
    virtual int getMessageType() const;
    virtual void setMessageType(int messageType);
    virtual double getAmount() const;
    virtual void setAmount(double amount);
    virtual int getPriorityClass() const;
    virtual void setPriorityClass(int priorityClass);
    virtual int getTransactionId() const;
    virtual void setTransactionId(int transactionId);
};

inline void doParsimPacking(omnetpp::cCommBuffer *b, const routerMsg& obj) {obj.parsimPack(b);}
inline void doParsimUnpacking(omnetpp::cCommBuffer *b, routerMsg& obj) {obj.parsimUnpack(b);}


#endif // ifndef __ROUTERMSG_M_H

